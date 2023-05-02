
const miOpcion=document.getElementById('micar2')
miOpcion.addEventListener('click', reproducir, false);

function reproducir(){
    const fuente=miOpcion.querySelector('source');
    const videoPrincipal=document.getElementById('micar1');
    videoPrincipal.source.src=fuente;
}
