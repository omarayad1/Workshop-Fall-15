$(function(){
    $('.submit-email').on('click', function(event){
    	console.log(event);
    	var email = $('.email').val();
    	var indexEmail = email.indexOf("@aucegypt.edu"); 
    	if (indexEmail === -1) {
    		alert('go home');
    		$('.email').css('background-color',"red");
    	}
    	else {
    		alert('welcome home');
    		$('.email').css('background-color',"green");
    	}
    });
});