




// el = element, clr = color

function changeBG(el) {
  let elem = document.getElementById(el)
  elem.classList.toggle('flipit')
  // elem.style.background = clr
} 






// function cardreverse() {
//   let cardToFlip = document.getElementById("flip3D");

//   if (cardToFlip.classList) { 
//     cardToFlip.classList.toggle("flipit");
//   } else {
//     let classes = cardToFlip.className.split(" ");
//     let i = classes.indexOf("flipit");

//     if (i >= 0) 
//       classes.splice(i, 1);
//     else 
//       classes.push("flipit");
//       cardToFlip.className = classes.join(" "); 
//   }
// }



// document.addEventListener('DOMContentLoaded', () => {

//   // Get all "navbar-burger" elements
//   const $flipButtons = Array.prototype.slice.call(document.querySelectorAll('.flip-button'), 0);

//   // Check if there are any navbar burgers
//   if ($flipButtons.length > 0) {

//     // Add a click event on each of them
//     $flipButtons.forEach($el => {
//       $el.addEventListener('click', function () {

//         // Get the target from the "data-target" attribute
//         const target = $el.dataset.target;
//         const $target = document.getElementById(target);

//         // Toggle the class on both the "navbar-burger" and the "navbar-menu"
//         $target.classList.toggle('flipit');
//       });
//     });
//   }
// });