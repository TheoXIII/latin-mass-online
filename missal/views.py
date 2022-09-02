from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.conf import settings
import os

base = os.path.join(settings.STATIC_PY_ROOT,'ordo')

parts = [
        os.path.join('pre_canon','incipit'),
        os.path.join('pre_canon','judica_me'),
        os.path.join('pre_canon','confiteor'),
        os.path.join('pre_canon','introit'),
        os.path.join('pre_canon','kyrie'),
        os.path.join('pre_canon','gloria'),
        os.path.join('pre_canon','collect'),
        os.path.join('pre_canon','epistle'),
        os.path.join('pre_canon','gradual'),
        os.path.join('pre_canon','munda'),
        os.path.join('pre_canon','gospel'),
        os.path.join('pre_canon','homily'),
        os.path.join('pre_canon','credo'),
        os.path.join('pre_canon','offertory'),
        os.path.join('pre_canon','suscipe'),
        os.path.join('pre_canon','lavabo'),
        os.path.join('pre_canon','secret'),
        os.path.join('pre_canon','preface'),
        os.path.join('pre_canon','sanctus'),
        os.path.join('canon','te_igitur'),
        os.path.join('canon','memento_living'),
        os.path.join('canon','communicantes'),
        os.path.join('canon','hanc_igitur'),
        os.path.join('canon','quam_oblationem'),
        os.path.join('canon','host'),
        os.path.join('canon','wine'),
        os.path.join('canon','memores'),
        os.path.join('canon','memento_dead'),
        os.path.join('canon','nobis_quoque'),
        os.path.join('post_canon','pater_noster'),
        os.path.join('post_canon','fracto_panis'),
        os.path.join('post_canon','agnus_dei'),
        os.path.join('post_canon','communion_priest'),
        os.path.join('post_canon','communion_laity'),
        os.path.join('post_canon','communion_prayer'),
        os.path.join('post_canon','post_communion'),
        os.path.join('post_canon','ite'),
        os.path.join('post_canon','placeat'),
        os.path.join('post_canon','benedicat'),
        os.path.join('post_canon','last_gospel'),
]

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def mass(request):
    if 'part' in request.GET:
        part = int(request.GET['part'])
    else:
        part = 0
    if (part < 0):
        part = 0
    elif (part >= len(parts)):
        part = len(parts)-1
    base_dir = os.path.join(base, parts[part])
    description = os.path.join(base_dir, 'description.html')
    image = os.path.join('ordo', parts[part], 'img.jpg')
    english = os.path.join(base_dir, 'default', 'english.html')
    latin = os.path.join(base_dir, 'default', 'latin.html')

    prev_url = reverse('mass')+'?part='+str(part-1)
    next_url = reverse('mass')+'?part='+str(part+1)

    context = {
            'description': description,
            'image': image,
            'english': english,
            'latin': latin,
            'prev_url': prev_url,
            'next_url': next_url,
            'grey_prev': part == 0,
            'grey_next': part == len(parts)-1,
    }
    template = loader.get_template('mass.html')
    return HttpResponse(template.render(context))
