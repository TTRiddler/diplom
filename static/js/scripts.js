$(document).ready(function() {

	$(".panel-body").hide().prev().click(function() {
		$(".panel-body").not(this).slideUp().prev().removeClass("active");
		$(this).next().not(":visible").slideDown().prev().addClass("active").css({"margin-bottom":"0"});
	});
});