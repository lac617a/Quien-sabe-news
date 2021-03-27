const btn_copy = document.getElementById('btnCopiar')
//Asigno el evento "click" del botón para provoar el copiado
btn_copy.addEventListener('click', copiarAlPortapapeles);

//Función que lanza el copiado del código
var codigoACopiar = document.getElementById('textoACopiar');    //Elemento a copiar
codigoACopiar.innerHTML = btn_copy.dataset.copy
function copiarAlPortapapeles(ev){
  //Debe estar seleccionado en la página para que surta efecto, así que...
  var seleccion = document.createRange(); //Creo una nueva selección vacía
  seleccion.selectNodeContents(codigoACopiar);    //incluyo el nodo en la selección
  //Antes de añadir el intervalo de selección a la selección actual, elimino otros que pudieran existir (sino no funciona en Edge)
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(seleccion);  //Y la añado a lo seleccionado actualmente
  try {
      var res = document.execCommand('copy'); //Intento el copiado
      if (res)
          exito();
      else
          fracaso();

      mostrarAlerta();
  }
  catch(ex) {
      excepcion();
  }
  window.getSelection().removeRange(seleccion);
}
///////
// Auxiliares para mostrar y ocultar mensajes
///////
var divAlerta = document.getElementById('alerta');

function callback(text_view){
  setTimeout(()=>{divAlerta.innerText = text_view;},500);
}
  
function exito() {
  divAlerta.classList.add('alert-success');
  callback('¡¡copiado con exito!!');
}

function fracaso() {
  divAlerta.classList.add('alert-warning');
  callback('¡¡Reintantalo!!');
}

function excepcion() {
  divAlerta.classList.add('alert-danger');
  callback('error al copiar al portapaples');
}

function mostrarAlerta() {
  divAlerta.classList.remove('invisible');
  divAlerta.classList.add('visible');
  setTimeout(ocultarAlerta, 2000);
}

function ocultarAlerta() {
  divAlerta.innerText = '';
  divAlerta.classList.remove('alert-success', 'alert-warning', 'alert-danger', 'visible');
  divAlerta.classList.add('invisible');
}