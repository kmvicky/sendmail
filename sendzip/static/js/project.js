/* Project specific Javascript goes here. */

var stopDefaultFormSubmit = function($form) {

	if($form === undefined) {

		$(".ui.form").on("submit", function(event) {

			event.preventDefault();
			return false;

		});

	}

	else {

		$form.on("submit", function(event) {
			
			event.preventDefault();
			return false;

		});

	}

}

var submitForm = function() {

	$form = $("form.ui.form");
	stopDefaultFormSubmit($form)

	$form.on("click", "input[type=submit]", function(event) {

		var data = $form.serializeArray()
			.filter(function(item){
				if(item.value != "") {
					return item;
				}
			});
		
		var url = $form.attr("action");

		$.ajax({
			method: "post",
			url: url,
			data: data
		}).done(function(response) {
			
			$("h5.error").html("Success");
			
		}).fail(function(xhr, responseJSON) {

			console.log("xhr = ", xhr.responseText);

			$("h5.error").html(xhr.responseText);
		});
	});


}


$(document).ready(function() {
	submitForm();
});
