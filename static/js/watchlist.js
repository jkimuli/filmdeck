$(document).ready(function(){

    var csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });

    $('.toast').toast();
    
    $('#watchButton').click(function(e){
    
        e.preventDefault();

        $.post('/movies/like',
         {
            movie_id: $(this).data('id'),
            title:$(this).data('title'),
            imagePath: $(this).data('image')

        },
            function(data){

                var message = data['status']
                $('.toast-body').append(message)
                $('.toast').toast('show')
        });

        $('.toast-body').empty() // reset div content

    });
});