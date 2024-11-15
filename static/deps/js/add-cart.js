$(document).ready(function() {   
    $(document).on('click', '#add-cart', function(e) {
        e.preventDefault();
        const url = $(this).data('url');
        const csrfToken = $(this).data('csrf-token');

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                vinyl_id: $(this).val(),
                csrfmiddlewaretoken: csrfToken,
                action: 'post'
            },
            success: function(json) {
                console.log(json);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});
