var hgt = $('#container'),
    bgt = $('#container .revealPic');

var bgtHalfW = bgt.width()/2,
    bgtHalfH = bgt.height()/2;

/**Change position of .revealPic and background-image within it on mousemove over container**/
hgt.mousemove(function(event){
    event.preventDefault();
    bgt.show();
    var scrollLeftPos = $(window).scrollLeft(),
    scrollTopPos = $(window).scrollTop(),
    offsetLft = hgt.offset().left,
    offsetTp = hgt.offset().top;
    var upX=event.clientX;
    var upY=event.clientY;
    bgt.css({backgroundPosition : ''+(offsetLft-upX+bgtHalfW-scrollLeftPos)+'px '+(offsetTp-upY+bgtHalfH-scrollTopPos)+'px',top:''+(-offsetTp+upY-bgtHalfH+scrollTopPos)+'px',left:''+(-offsetLft+upX-bgtHalfW+scrollLeftPos)+'px'});
});
/*********************************************/

/*Hide .revealPic div on mouseout*/
hgt.mouseout(function(){
    bgt.hide();
});
/*********************************/

/*Using vague.js to make blurred image*/
var vague = $("#container img").Vague({intensity:10});
vague.blur();
/**************************************/
