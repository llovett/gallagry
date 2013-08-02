(function ($) {
    $.fn.breathe = function( options ) {
	var settings = $.extend({
	    speed: 5000,
	    amount: 0.1
	}, options);

	this.wrap("<div>");
	var transformed = this.parent("div");
	transformed.css("display", "inline-block");
	
	var breathe2 = function() {
	    $(this).transition({
		scale: 1+settings.amount
	    }, { duration:settings.speed });
	    $(this).transition({
		scale: 1-settings.amount
	    }, { duration:settings.speed, complete:breathe2 });
	};
	// var breathe = function() {
	//     this.transition({
	// 	scale: 1+settings.amount
	//     }, { duration:settings.speed });
	//     this.transition({
	// 	scale: 1-settings.amount
	//     }, { duration:settings.speed, complete:breathe2 });
	// };
	breathe2.call(transformed);

	return this;
    };
})(jQuery);
