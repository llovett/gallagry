$(document).ready(
    function() {
	// CSRF protection
	// source: https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
		    var cookie = jQuery.trim(cookies[i]);
		    // Does this cookie string begin with the name we want?
		    if (cookie.substring(0, name.length + 1) == (name + '=')) {
			cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
			break;
		    }
		}
	    }
	    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	function sameOrigin(url) {
	    // test that a given url is a same-origin URL
	    // url could be relative or scheme relative or absolute
	    var host = document.location.host; // host + port
	    var protocol = document.location.protocol;
	    var sr_origin = '//' + host;
	    var origin = protocol + sr_origin;
	    // Allow absolute or scheme relative URLs to same origin
	    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
		// or any other URL that isn't scheme relative or absolute i.e relative.
		!(/^(\/\/|http:|https:).*/.test(url));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
		    // Send the token to same-origin, relative URLs only.
		    // Send the token only if the method warrants CSRF protection
		    // Using the CSRFToken value acquired earlier
		    xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	    }
	});

	// Editing link orientation and position
	var matrices;

	$("#edit_btn").click(
	    function() {
		$(".main_page_link").each(function(){$(this).freetrans();});
		matrices = new Array();
	    }
	);

	$("#done_btn").click(
	    function() {
		$(".main_page_link").each(
		    function() {
			var link_id = $(this).prop("id").split("_");
			link_id = link_id[link_id.length-1];
			link_id = (link_id === 'link' ?  "gallery" : link_id);
			matrices.push({"link_id":link_id,
				       "angle":$(this).data('freetrans').angle,
				       "top":$(this).data('freetrans').y,
				       "left":$(this).data('freetrans').x});
			$(this).freetrans('destroy');
		    }
		);

		console.log(matrices);

		// TODO: submit this for saving server-side
		$.post("/edit/", JSON.stringify({"transforms":matrices}));
	    }
	);
    }
);
