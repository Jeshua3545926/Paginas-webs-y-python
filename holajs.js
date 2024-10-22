class BotonHandler{
    constructor(clase){
        this.botones = document.querySelectorAll("." + clase);
        this.agregarEventos();
    }

agregarEventos(){

this.botones.forEach(boton => {
    boton.addEventListener("click",() => {
    this.mostrarMensaje();
  });
});

}


mostrarMensaje(){

alert("AGREGADO AL CARRITO CORRECTAMENTE");

}

}
const botonesRegresar = new BotonHandler("btn-agregar");