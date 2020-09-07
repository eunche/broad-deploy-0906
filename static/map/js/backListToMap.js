const backListToMap = () => {
  newContent.remove();
  body.classList.add("set_fixed");
  content.classList.remove("set_none");
  header.innerHTML = beforeHeader;
  document.querySelector("body").classList.remove("overflow_none");
};
