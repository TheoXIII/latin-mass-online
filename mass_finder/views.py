from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Churches
from django.db.models import Q, F, IntegerField, Value
from functools import partial


def index(request):
    template = loader.get_template('finder.html')
    churches = Churches.objects.all()
    if request.method == 'POST':
        terms = request.POST['term'].strip()
        low_mass = 'low' in request.POST
        sung_mass = 'sung' in request.POST
        high_mass = 'high' in request.POST
        churches_filtered = Churches.objects.none()
        counts = {}
        def countsorter(church):
            return counts.get(church.id, 0)
        for term in terms.split(" "):
            returned_churches = churches.filter(name__icontains=term) | \
            churches.filter(address__icontains=term)
            for church in returned_churches:
                if church.id in counts.keys():
                    counts[church.id] += 1
                else:
                    counts[church.id] = 0
            churches_filtered = churches_filtered | returned_churches
        churches = churches_filtered.filter(Q(low_mass=low_mass) | Q(low_mass=True), Q(sung_mass=sung_mass) | Q(sung_mass=True),Q(high_mass=high_mass) | Q(high_mass=True))
        churches = sorted(churches, key=countsorter, reverse=True)
        context = {
            'search': terms,
            'low_mass': low_mass,
            'sung_mass': sung_mass,
            'high_mass': high_mass,
            'churches': churches,
        }
    else:
        context = {
                'churches': churches,
        }
    return HttpResponse(template.render(context, request))

def church(request):
    if 'id' in request.GET:
        ident = int(request.GET['id'])
    else:
        ident = 1
    info = Churches.objects.filter(id=ident).values()
    template = loader.get_template('church.html')
    context = {
            'info': info[0],
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    name = request.POST['name']
    location = request.POST['location']
    address = request.POST['address']
    mass_times = request.POST['times']
    website = request.POST['website']
    image_url = request.POST['image']
    low_mass = False
    sung_mass = False
    high_mass = False
    if 'low' in request.POST:
        low_mass = True
    if 'sung' in request.POST:
        sung_mass = True
    if 'high' in request.POST:
        high_mass = True
    church = Churches(name=name, location=location, address=address, mass_times=mass_times,
            website=website, image_url=image_url, low_mass=low_mass, sung_mass=sung_mass,
            high_mass=high_mass)
    church.save()
    return HttpResponseRedirect(reverse('add'))

def edit(request):
    template = loader.get_template('edit.html')
    ident = request.GET['id']
    church = Churches.objects.get(id=ident)
    context = {
            'id': ident,
            'name': church.name,
            'location': church.location,
            'address': church.address,
            'mass_times': church.mass_times,
            'image_url': church.image_url,
            'website': church.website,
            'low_mass': church.low_mass,
            'sung_mass': church.sung_mass,
            'high_mass': church.high_mass,
    }
    return HttpResponse(template.render(context,request))


def editrecord(request):
    ident = request.POST['id']
    name = request.POST['name']
    location = request.POST['location']
    address = request.POST['address']
    mass_times = request.POST['times']
    website = request.POST['website']
    image_url = request.POST['image']
    low_mass = False
    sung_mass = False
    high_mass = False
    if 'low' in request.POST:
        low_mass = True
    if 'sung' in request.POST:
        sung_mass = True
    if 'high' in request.POST:
        high_mass = True
    church = Churches.objects.get(id=ident)
    church.name=name
    church.location=location
    church.address=address
    church.mass_times=mass_times
    church.website=website
    church.image_url=image_url
    church.low_mass=low_mass
    church.sung_mass=sung_mass
    church.high_mass=high_mass
    church.save()
    return HttpResponseRedirect(reverse('index'))

def deleterecord(request):
    ident = request.POST['id']
    church = Churches.objects.get(id=ident)
    church.delete()
    return HttpResponseRedirect(reverse('index'))
