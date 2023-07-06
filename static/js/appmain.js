/*---------------------------
 appmain
 submit.html - #btn_execute
---------------------------*/
$(function () {
    $('#btn_execute').off().on("click", function () {

        $("#area4Result").empty();  // clear result area

        var command = $("#selected_dropdown_item").val();  // Submit_an_image
        console.log("[appmain.js] command= ", command);

        var file_name = $('#dataFile').prop('files')[0].name;
        console.log("[appmain.js] file_name= ", file_name);

        // formData for POST
        var formData = new FormData($('#uploadForm')[0]);  //FormData object
        formData.append("command", command);
        formData.append('file_name', file_name);

        // deactivate button
        $('#btn_execute').prop("disabled", true);
        $('#btn_execute').text("Executing...");

        // const csrftoken = getCookie('csrftoken');
        // console.log('[topview.js] csrftoken= ', csrftoken);  // in this case, csrftoken is null

        $.ajax({
            url: 'appmain/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            encType: 'multipart/form-data',
        })
            .done(function (output, status, xhr) {
                $('#area4Result').html(output);
                $('#area4Result').show();

                // activate button
                $('#btn_execute').prop("disabled", false);
                $('#btn_execute').text("Execute");

            })
            .fail(function (error) {
                console.log(error);
            });  // ajax
    });  // function
});  // function
