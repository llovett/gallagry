$(document).ready(
    function() {
	$(".gallery_preview").hover(
	    function() {
		$(this).next(".gallery_description").toggle();
	    }
	);
    }
);
