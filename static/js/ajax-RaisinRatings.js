$(document).ready(function(){
    $('#like-btn-cat').click(function() {
        var categoryNameVar;
        categoryNameVar = $(this).attr("data-categoryname");

        $.get('/RaisinRatings/like_category/',
            {'name': categoryNameVar},
            function(data){
                $('#like_count').html(data + " likes");
                $('#like-btn_cat').hide();
        })
    });

    $('#dislike-btn-cat').click(function(){
        var categoryNameVar;
        categoryNameVar = $(this).attr("data-categoryname");
        $.get('/RaisinRatings/dislike_category/',
        {'name':categoryNameVar},
        function(data){
            $('#like_count').html(data + " likes"); 
            $('#dislike-btn_cat').hide();
        })
    });

    $('#like-btn-movie').click(function(){
        var movieNameVar;
        movieNameVar = $(this).attr("data-moviename");
        $.get('/RaisinRatings/like_movie/',
        {'movie_name':movieNameVar},
        function(data){
            $('#like_count').html(data + " likes")
        })
    })

    $('#dislike-btn-movie').click(function(){
        var movieNameVar;
        movieNameVar = $(this).attr("data-moviename");
        $.get('/RaisinRatings/dislike_movie/',
        {'movie_name':movieNameVar},
        function(data){
            $('#like_count').html(data + " likes")
        })
    })

});