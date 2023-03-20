console.log("stars.js loaded");
function hoverStar(star) {
  // Get all the star elements and loop through them
  var stars = document.querySelectorAll('.fa-star');
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

// Get all the star elements and loop through them
var stars = document.querySelectorAll('.fa-star');
for (var i = 0; i < stars.length; i++) {
  // Add a mouseover event listener to each star element
  stars[i].addEventListener('mouseover', function() {
    hoverStar(this);
  });
}

const star1 = document.getElementById('star1');
  console.log('star1 mouseover');
star1.addEventListener('mouseover', function starOver() {
  console.log('star1 mouseover');
  star1.style.color = 'red';
});


