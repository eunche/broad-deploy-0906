const backDetailToMap = () => {
  detailContent.remove();
  body.classList.add("set_fixed");
  content.classList.remove("set_none");
  document.querySelector("body").classList.remove("overflow_none");
  document.querySelector("header").innerHTML = mapHeader;
};
