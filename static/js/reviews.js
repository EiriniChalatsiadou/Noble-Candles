/* jshint esversion: 6 */
/* globals $:false */

$('.star').click(function(e) {
    // Select all previous stars before the clicked star
    let prevStars = $(this).parent().prevAll('label').children();
    
    // Select all stars within the same parent container
    let allStars = $(this).parent().parent().children('label').children();
    
    // Reset all stars to empty (far) stars
    allStars.removeClass('fas').addClass('far');
    
    // Fill the clicked star and all previous stars with filled (fas) stars
    $(this).removeClass('far').addClass('fas');
    prevStars.removeClass('far').addClass('fas');
});
