/* Cree la función JavaScript mostrarFecha(), la que debe desplegar la fecha y hora
  actuales en formato “Hoy es [DIA SEMANA] [DIA] de [MES] de [AÑO], y son las [HORA]
  horas, [MINUTOS] minutos con [SEGUNDOS] segundos”. El campo [DIA SEMANA] debe
  ser de texto correspondiente al día de la semana.
  Esta función debe estar declarada en un archivo .js independiente. Debe enlazarlo
  desde una página web de nombre ejercicio11.html, y debe llamar a la función una vez
  que abra la página, desplegando su retorno a través de un mensaje de alerta. Al
  mismo tiempo, debe escribir en un contenedor con identificador o id igual a
  “tiemporestante” el tiempo que queda en días, minutos y segundos para que termine
  el año.
  Se solicita que en este ejercicio se aplique un diseño basado en estilos CSS, en un
  archivo independiente enlazado desde la página web creada. Debe tener, al menos:
  ● Imagen de fondo
  ● Fuente de encabezados y de párrafos distintos
  ● Use colores distintos para las letras
  ● El borde del contenedor “tiemporestante” debe estar con un diseño especial*/

function mostrarFecha(){
const second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;
     
      const dayarray = new Array("DOMINGO", "LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO")
     
      const montharray = new Array("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")
      
      var fechadia =  new Date().getDay(),
      d = dayarray[fechadia]

      var fechames =  new Date().getMonth(),
       m = montharray[fechames]

      var fechaano =  new Date().getFullYear(),
       a =  fechaano
  
      var dian =new Date().getDay(),
       n = dian -1
       alert("hoy es "+(d)+" "+(n)+" de "+(m)+" del "+(a));


      let countDown = new Date('Dec 31, 2022 00:00:00').getTime(),
    x = setInterval(function() {

      let now = new Date().getTime(),
          distance = countDown - now;

      let fechadia =  new Date().getDay(),
          d = dayarray[fechadia]

      let fechames =  new Date().getMonth(),
          m = montharray[fechames]

      let fechaano =  new Date().getFullYear(),
          a =  fechaano
      
      let dian =new Date().getDay(),
          n = dian -1
      

        document.getElementById('dias').innerText = Math.floor(distance / (day)),
        document.getElementById('horas').innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById('minutos').innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById('segundos').innerText = Math.floor((distance % (minute)) / second),
        document.getElementById('dia').innerText = ((d)),
        document.getElementById('mes').innerText = ((m)),
        document.getElementById('ano').innerText = ((a)),
        document.getElementById('dianum').innerText = ((n)); 
       
        
       
        
        

    }, second)
    
  }
  mostrarFecha();
