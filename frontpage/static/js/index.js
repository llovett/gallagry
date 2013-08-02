$(document).ready(function(){
    // Marquee scrolling solution from http://stackoverflow.com/questions/2143056/seamless-jquery-marquee
    var marquee = $("#gallery-marquee");

    marquee.css({"overflow": "hidden", "width": "420px", "height": "200px"});

    // wrap "My Text" with a span (old versions of IE don't like divs inline-block)
    marquee.wrapInner("<span>");
    marquee.find("span").css({ "width": "50%", "display": "inline-block", "text-align":"center" }); 
    marquee.append(marquee.find("span").clone()); // now there are two spans with "My Text"

    // create an inner div twice as wide as the view port for animating the scroll
    marquee.wrapInner("<div>");
    marquee.find("div").css("width", "200%");

    // create a function which animates the div
    // $.animate takes a callback for when the animation completes
    var reset = function() {
        $(this).css("margin-left", "0%");
        $(this).animate({ "margin-left": "-100%" }, 3000, 'linear', reset);
    };

    // kick it off
    reset.call(marquee.find("div"));
});
