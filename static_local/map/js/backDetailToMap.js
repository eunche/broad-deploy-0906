const backDetailToMap = () => {
  detailContent.remove();
  content.classList.remove("set_none");
  document.querySelector("header").innerHTML = mapHeader;
  document
    .querySelector("#map")
    .setAttribute("style", `height:${viewHeight}px;`);
};
