$(document).ready(
    function() {
	$('.gallery_image').hover(
	    function() {
		$(this).parent().prev().toggle();
	    }
	);
    }
);
