$(document).ready(function(){
    $('#like-btn-movie').click(function() {
        var movieNameVar;
        movieNameVar = $(this).attr("data-moviename");

        $.get('/RaisinRatings/like_movie/',
            {'name': movieNameVar},
            function(data){
                $('#like_count').html(data + " likes");
                $('#like-btn_cat').hide();
        })
    });

});