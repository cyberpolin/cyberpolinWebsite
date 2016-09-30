$(document).ready(function(){
  //Get the action
  $('form').on('submit', function(e){
    // Getting every item in the form
    // TODO: catch more than one form
    var formErrors = 0;
    var input = ($(this).find('input[type=text]'));
    for (var i = 0; i < input.length; i++){
      if ($(input[i]).val().trim() == ''){
        $(input[i]).attr('style', 'border:1px solid red');
        formErrors++;

      } else {
        $(input[i]).attr('style', 'border:1px solid green');

      }
      $(input[i]).val();
    }
    console.log(formErrors);
    if (formErrors != 0) {
      e.preventDefault();
    }
  });
});
