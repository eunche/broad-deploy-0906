const backListToMap = () => {
  newContent.remove();
  body.classList.add("set_fixed");
  content.classList.remove("set_none");
  header.innerHTML = beforeHeader;
  document
    .querySelector("body")
    .setAttribute(
      "style",
      `height:${viewHeight}px; max-height:${viewHeight}px;`
    );
  document.documentElement.scrollTop = 0;
};
