$(document).ready(
    function() {
	$(".gallery_link").hover(
	    function() {
		$(this).find(".gallery_description").toggle();
	    }
	);
    }
);
