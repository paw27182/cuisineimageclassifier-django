/*---------------------------
 execute
 submit.html - #btn_execute
---------------------------*/
$(function(){
	$('#btn_execute').off().on("click", function(){

	    $("#area4Result").empty();  // clear result area

        var command = $("#selected_dropdown_item").val();  // Submit_an_image
        console.log("[execute.js] command= ", command);

        var file_name = $('#dataFile').prop('files')[0].name;
        console.log("[execute.js] file_name= ", file_name);

        // formData for POST
        var formData = new FormData($('#uploadForm')[0]);  //FormData object
        formData.append("command", command);
        formData.append('file_name', file_name);

        // deactivate button
        $('#btn_execute').prop("disabled", true);
        $('#btn_execute').text("Executing...");

		$.ajax({
			url: 'execute/',
			type: 'POST',
			data: formData,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
            })
			.done(function(output, status, xhr){
                $('#area4Result').html(output);
                $('#area4Result').show();

				// activate button
			    $('#btn_execute').prop("disabled", false);
			    $('#btn_execute').text("Execute");

			})
			.fail(function(error){
				console.log(error);
			});  // ajax
	});  // function
});  // function
