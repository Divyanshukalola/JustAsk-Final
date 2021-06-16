/**
* Template Name: Bootslander - v2.2.0
* Template URL: https://bootstrapmade.com/bootslander-free-bootstrap-landing-page-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/


*/
!(function($) {
  "use strict";



  $("#success-alert").hide();
   $("#success-alert").fadeTo(2000, 500).delay(60000).fadeOut(500, function() {
      $("#success-alert").fadeOut(500);
    });



    /* Enable for stop screen shots*/

  document.addEventListener("keyup", function (e) {
    var keyCode = e.keyCode ? e.keyCode : e.which;
            if (keyCode == 44 || keyCode == 91 || keyCode == 93 || keyCode == 51 || keyCode == 18) {
                stopPrntScr();
            }
        });
function stopPrntScr() {

            var inpFld = document.createElement("input");
            inpFld.setAttribute("value", ".");
            inpFld.setAttribute("width", "0");
            inpFld.style.height = "0px";
            inpFld.style.width = "0px";
            inpFld.style.border = "0px";
            document.body.appendChild(inpFld);
            inpFld.select();
            document.execCommand("copy");
            inpFld.remove(inpFld);
        }
       function AccessClipboardData() {
            try {
                window.clipboardData.setData('text', "Access   Restricted");
            } catch (err) {
            }
        }
        setInterval("AccessClipboardData()", 300);  







  
 if(!sessionStorage.isVisited){
 	document.getElementById("preloader1").hidden = false;
    $(window).on('load', function() {
        
        if ($('#preloader1').length) {
         sessionStorage.isVisited = 'true';
        $('#preloader1').delay(1000).fadeOut('slow', function() {
          $(this).remove();
        });
        }
      
    });
}
else{
    document.getElementById("preloader").hidden = false;
    document.getElementById("preloader1").hidden = true;
    /*$("#feedbackModal").modal({show: false});*/
       
    }



      // Preloader
  $(window).on('load', function() {
    if ($('#preloader').length) { 
      $('#preloader').delay(100).fadeOut('slow', function() {
        $(this).remove();
      });
    }
  });

  // Smooth scroll for the navigation menu and links with .scrollto classes
  var scrolltoOffset = $('#header').outerHeight() - 21;
  $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function(e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();

        var scrollto = target.offset().top - scrolltoOffset;

        if ($(this).attr("href") == '#header') {
          scrollto = 0;
        }

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Activate smooth scroll on page load with hash links in the url
  $(document).ready(function() {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });

  // Mobile Navigation
  if ($('.nav-menu').length) {
    var $mobile_nav = $('.nav-menu').clone().prop({
      class: 'mobile-nav d-lg-none'
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
    $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
      $('.mobile-nav-overly').toggle();
    });

    $(document).on('click', '.mobile-nav .drop-down > a', function(e) {
      e.preventDefault();
      $(this).next().slideToggle(300);
      $(this).parent().toggleClass('active');
    });

    $(document).click(function(e) {
      var container = $(".mobile-nav, .mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }



    

    /*// Navigation active state on scroll
    var nav_sections = $('main');
    var main_nav = $('.nav-menu, .mobile-nav');

    $(window).on('load', function() {
      var cur_pos = $(this).scrollTop() + 200;

      nav_sections.each(function() {
        var top = $(this).offset().top,
          bottom = top + $(this).outerHeight();

        if (cur_pos >= top && cur_pos <= bottom) {
          if (cur_pos <= bottom) {
            main_nav.find('li').removeClass('active');
          }
          if ($(this).attr('id') == ''){
            main_nav.getElementById('home').addClass('active');
            
          }else{
            main_nav.find('a[href="/' + $(this).attr('id') + '"]').parent('li').addClass('active');
            main_nav.getElementById('home').removeClass('active');
          }
          
          
        }
        if (cur_pos < 300) {
          $(".nav-menu ul:first li:first, .mobile-menu ul:first li:first").addClass('active');
        }
      });
    });*/

  // Toggle .header-scrolled class to #header when page is scrolled
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
    } 
  });

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
  }

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 50) {
      $('.back-to-top').fadeIn('slow');
      /*$('.back-to-top2').fadeIn('slow');*/
    } else {
      $('.back-to-top').fadeOut('slow');
      /*$('.back-to-top2').fadeOut('slow');*/

    }
  });


  


  $('.back-to-top').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Initiate the venobox plugin
  $(window).on('load', function() {
    $('.venobox').venobox();
  });

  // jQuery counterUp
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 1000
  });

  // Initiate venobox lightbox
  $(document).ready(function() {
    $('.venobox').venobox();
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Init AOS
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  }
  $(window).on('load', function() {
    aos_init();
  });

})(jQuery);


              




/*Below is the code for paypal buttons just to save it i am keeping it here
*/


/* <script>
        // Render the PayPal button into #paypal-button-container
        function completeOrder(){
          var url = "/payment_mntly"

          window.location.href = url;
        }


        paypal.Buttons({
          style: {
                color:  'blue',
                shape:  'pill',
                label:  'pay',
                height: 40
            },


            // Set up the transaction
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: '7.95'
                        }
                    }]
                });
            },

            // Finalize the transaction
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(details) {
                    // Show a success message to the buyer
                    completeOrder()
                    alert('Transaction completed by ' + details.payer.name.given_name + '!');
                });
            }


        }).render('#paypal-button-container-m');
    </script>


     <script>
        // Render the PayPal button into #paypal-button-container
        function completeOrder1(){
          var url = "/payment_yrly"

          window.location.href = url;
        }


        paypal.Buttons({
          style: {
                color:  'blue',
                shape:  'pill',
                label:  'pay',
                height: 40
            },


            // Set up the transaction
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: '72.89'
                        }
                    }]
                });
            },

            // Finalize the transaction
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(details) {
                    // Show a success message to the buyer
                    completeOrder1()
                    alert('Transaction completed by ' + details.payer.name.given_name + '!');
                });
            }


        }).render('#paypal-button-container-y');
    </script>



      <script>
        // Render the PayPal button into #paypal-button-container
        var fees = 0;
        function customAmount(){
          fees = document.getElementById("donate").value;
        }

        function Amount1(){
          fees = 5;
        }

        function Amount2(){
          fees = 10;
        }

        function Amount3(){
          fees = 20;
        }

        function completeOrder(){
          var url = "/TYDONATE"

          window.location.href = url;
        }


        paypal.Buttons({
          style: {
                color:  'blue',
                shape:  'pill',
                label:  'pay',
                height: 40
            },


            // Set up the transaction
            createOrder: function(data, actions) {
                return actions.order.create({
                    purchase_units: [{
                        amount: {
                            value: fees
                        }
                    }]
                });
            },

            // Finalize the transaction
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(details) {
                    // Show a success message to the buyer
                    completeOrder()
                    alert('Transaction completed by ' + details.payer.name.given_name + '!');
                });
            }


        }).render('#paypal-button-container4');
    </script>*/

