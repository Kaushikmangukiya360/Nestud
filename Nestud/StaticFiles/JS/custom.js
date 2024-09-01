$(window).scroll(function(){
    if ($(window).scrollTop() >= 330) {
      $('.sticky-wrapper').addClass('fixed');
     }
     else {
      $('.sticky-wrapper').removeClass('fixed');
     }
  });

$(document).ready(function () {
    $(".testimonial-active").slick({
        slidesToShow: 3,
        infinite: false,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
        dots: true,
    });

    $(".open-popup-btn-event").click(function(){
        $(".event-form-popup").addClass("event-popup-active");
        $("body").addClass("event-model-open");
      });
      $(".event-popup-close-btn").click(function(){
        $(".event-form-popup").removeClass("event-popup-active");
        $("body").removeClass("event-model-open");
      });
});

