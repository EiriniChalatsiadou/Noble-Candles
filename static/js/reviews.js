// Changes stars from empty to filled on selection
    $('.star').click(function(e) {
        prevStars = $(this).parent().prevAll('label').children();
        allStars = $(this).parent().parent().children('label').children();
        
        allStars.removeClass('fas').addClass('far');
        $(this).removeClass('far').addClass('fas');
        prevStars.removeClass('far').addClass('fas');
    });