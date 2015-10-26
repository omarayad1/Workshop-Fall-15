$(function(){
    $('.validate').on('change', function(event){
    	var email = $('.validate').val();
    	var indexEmail = email.indexOf("@aucegypt.edu"); 
    	if (indexEmail === -1) {
    		$('.alert-container').html('<div class="alert alert-danger" role="alert">Go Home</div>');
    	}
    	else {
    		$('.alert-container').html('<div class="alert alert-success" role="alert">Welcome Home</div>');
    	}
    });
    $(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
});