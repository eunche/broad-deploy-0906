const backDetailToMap = () => {
  detailContent.remove();
  content.classList.remove("set_none");
  document.querySelector("header").innerHTML = mapHeader;
  document
    .querySelector("body")
    .setAttribute(
      "style",
      `height:${viewHeight}px; max-height:${viewHeight}px;`
    );
  document.documentElement.scrollTop = 0;
};
