document.addEventListener('DOMContentLoaded', function() {
   document.getElementById("login-btn").disabled = true;
   document.onkeyup = () => {
     if (document.getElementById("email-login").value.length > 0) and (document.getElementById("password-login").value.length > 0)) {
      document.getElementById("login-btn").disabled = false;
      }
     else {
      document.getElementById("login-btn").disabled = true;
      }
 }
});
