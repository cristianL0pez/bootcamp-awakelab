/*
- Crea un nuevo archivo de nombre funciones.js.
- Crea una función en JavaScript que permita validar todos los campos del formulario de contacto
al momento de hacer clic en el botón de procesamiento. Se debe indicar qué campos están
vacíos.
- Es fundamental que enlaces este nuevo archivo al documento HTML respectivo.
- Si bien llamarás al archivo JavaScript desde un solo archivo, es conveniente que todos los
documentos del proyecto llamen a este archivo.*/



document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
  });
  
  function validarFormulario(evento) {
  evento.preventDefault();
    var usuario = document.getElementById('usuario').value;
    if(usuario.length == 0) {
      alert('No has escrito nada en el usuario');
      return;      
    }  
    var email= document.getElementById('mail').value;
    if (email.length == 0) {
      alert('el email no es valido ');
      return;
    }
    var areatext= document.getElementById('areatext').value;
    if (areatext.length < 20) {
      alert('por favor escribe un mensaje');
      return;
    }
    this.submit();
  }
  



 



