//Fucntions for scroll spy, clicking links on page will scroll down to appropriate section

$(function () {
	$(window).on("load resize", function () {
		$(".fill-screen").css("height", window.innerHeight)
	});

	$('body').scrollspy({
		target: '.navbar',
		offset: 200
	});
});


//Offset on scroll to stay below nav bar
var offset = 50;
$('.navbar li a').click(function(event) {
    event.preventDefault();
    $($(this).attr('href'))[0].scrollIntoView();
    scrollBy(0, -offset);
});


