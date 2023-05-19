// // $(function(){
	
// // });

// $(document).ready(function () {
//     $(".typed").typed({
// 		strings: ["Seo", "Designers", "Software"],
// 		stringsElement: null,
// 		typeSpeed: 80,
// 		backSpeed: 80,
// 		backDelay: 800,
// 		loop: true,
// 	});
// });

// Can also be included with a regular script tag
// import Typed from 'typed.js';

// var options = {
//   strings: ['<i>First</i> sentence.', '&amp; a second sentence.'],
//   typeSpeed: 40
// };

// var typed = new Typed('.element', options);

var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    strings: [
      'HTML',
      'CSS',
      'BOOTSTRAP',
      'JAVASCRİPT',
      'REACT',
      'PYTHON',
      'DJANGO',
      'C#',
      '.NET',
      'C++',
    ],
    stringsElement: null,
    typeSpeed:40,
    loop:true
});


$(document).ready(function() {
  // butona tıklandığında
  $('.button-main a').click(function(e){
    // varsayılan davranışı engelleyin
    e.preventDefault();
    
    // main.html sayfasını yukarı doğru kayarak kaybolmasını sağlayın
    $('body').slideUp(1000, function(){
      // yönlendirme yapın
      window.location.href = "login.html";
    });

    // Arka plan rengini değiştirin
    $('body').css('background-color', '#333');
  });
});

