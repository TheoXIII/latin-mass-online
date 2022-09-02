window.onload = function() {
  let frameElement = document.getElementById("coloured");
  console.log(frameElement);
  let doc = frameElement.contentDocument;
  doc.body.innerHTML = doc.body.innerHTML + '<style>.red {color:red;}</style>';

  console.log(doc.body.innerHTML);
}
