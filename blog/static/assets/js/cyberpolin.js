$(function() {
	var pattern = '/static/assets/img/overlays/'+Math.floor((Math.random() * 15) + 1)+'.png';
	imagenes = [
	    { src:'/static/assets/img/wall-papers/angular developer-desk.jpg', fade:2000 },
	    { src:'/static/assets/img/wall-papers/django-developer-family.jpg', fade:2000 },
	    { src:'/static/assets/img/wall-papers/web-developer-bike.jpg', fade:2000 },
	    { src:'/static/assets/img/wall-papers/front-end-developer-vehicle.jpg', fade:2000 }
	  ];
	  wallPaperRND = Math.floor((Math.random() * imagenes.length)+1);

	$.vegas('slideshow', {
	  delay:15000,
	  backgrounds:imagenes,
	  step: wallPaperRND,
	  walk: function(step){
	  	//$.vegas('jump', wallPaperRND)
	  	('overlay', {src:pattern});
	  }
	})('overlay', {
	src:pattern});
});	

$(function() {
	var height = $(window).height();
	var carousel = $('.portfolio');
	var except = $('.container').height();
	carousel.height(height-except);

});	