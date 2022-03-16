document.querySelector('#placeOrder').disabled = true;
  document.onkeyup = () => {
    if (document.querySelector('#firstName').value.length > 0) and (document.querySelector('#address').value.length > 0)) {
      document.querySelector('#placeOrder').disabled = false;
    }
    else {
      document.querySelector('#placeOrder').disabled = true;
    }
  }
