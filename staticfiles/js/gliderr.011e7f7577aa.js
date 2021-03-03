window.onload = function(){
  new Glider(document.querySelector('.carousel-list'),{
    // allow mouse dragging
    draggable: true,
    // dot container element or selector
    dots: '.carousel-dots',
  });
}