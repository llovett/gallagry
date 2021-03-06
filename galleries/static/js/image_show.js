$(document).ready(
    function() {
	// Calculate width of body
	var total_width = 0;
	var win_width = $(window).width();
	var images = $(".gallery_image");
	if (images.length > 0) {
	    images.each(
		function(index, el) {
		    // 6px padding on side of each image
		    total_width += 12 + $(this).width();
		}
	    );
	    // 10px padding on wrapper, gallery on each side, plus some as buffer
	    total_width += 50;

	    console.log(total_width);
	    $("body").css('width',(total_width < win_width ? win_width : total_width)+"px");
	}
    }
);
