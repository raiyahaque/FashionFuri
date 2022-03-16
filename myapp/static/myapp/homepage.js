document.addEventListener('DOMContentLoaded', function() {

   // Find heading
   const h1 = document.querySelector('#logo');

   // Pause Animation by default
   h1.style.animationPlayState = 'paused';

   // Wait for button to be clicked
   document.querySelector('a').onclick = () => {

      // If animation is currently paused, begin playing it
      if (h1.style.animationPlayState == 'paused') {
            h1.style.animationPlayState = 'running';
         }

      // Otherwise, pause the animation
      else {
         h1.style.animationPlayState = 'paused';
      }
   }

});
