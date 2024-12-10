function doalert(checkboxElem) {

  let bg = document.getElementById("ColorBg");

  if (checkboxElem.checked) {
    bg.setAttribute("disabled", "");
  } else {
    bg.removeAttribute("disabled");
  }
}
