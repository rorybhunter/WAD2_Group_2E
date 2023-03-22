console.log("stars.js loaded");
var isClicked = false
function hoverStar(star) {
  // Get all the star elements and loop through them
    var stars = document.querySelectorAll('.fa-star');
    if (isClicked === false) {
        for (var i = 0; i < stars.length; i++) {
            // If the current star is to the left of the hovered star or is the hovered star, add the "checked" class
            if (stars[i].id <= star.id) {
                stars[i].classList.add('checked');
            }
            // Otherwise, remove the "checked" class
            else {
                stars[i].classList.remove('checked');
            }
        }
    }
}


function offStarDiv() {
  // Get all the star elements and loop through them
    var stars = document.querySelectorAll('.fa-star');
    if (isClicked === false) {
        for (var i = 0; i < stars.length; i++) {
            // Remove the "checked" class
            stars[i].classList.remove('checked');
        }
    }
}

function clickKeep(star) {
    // When star is clicked, add the "checked" class and keep the checked class
    var stars = document.querySelectorAll('.fa-star');
    if (isClicked === false) {
        for (var i = 0; i < stars.length; i++) {
            if (stars[i].id <= star.id) {
                 stars[i].classList.add('checked');
            }
        }
        isClicked = true
        var starnum = parseInt(star.id.slice(-1));

        // find html element with name starnum and set its value to starnum
        console.log(starnum);
        document.querySelector('input[name="starnum"]').value = starnum;
    }
    else {
        for (var i = 0; i < stars.length; i++) {
            stars[i].classList.remove('checked');
        }
        isClicked = false
    }

}

// Get all the star elements and loop through them
var stars = document.querySelectorAll('.fa-star');
var div = document.getElementById('stars');
for (var i = 0; i < stars.length; i++) {
    // Add a mouseover event listener to each star element
    stars[i].addEventListener('mouseover', function() {
      hoverStar(this);
    });
    stars[i].addEventListener('mouseout', function() {
      offStarDiv();
    });
      stars[i].addEventListener('click', function() {
          clickKeep(this);
      });
}