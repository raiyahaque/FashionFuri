document.querySelector('#register-btn').disabled = true;
  document.onkeyup = () => {
    if (document.querySelector('#register_email').value.length > 0) and (document.querySelector('#register_username').value.length > 0)) {
      document.querySelector('#register-btn').disabled = false;
    }
    else {
      document.querySelector('#register-btn').disabled = true;
    }
  }
