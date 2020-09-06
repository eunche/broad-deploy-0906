const backListToMap = () => {
  newContent.remove();
  content.classList.remove("set_none");
  header.innerHTML = beforeHeader;
  document
    .querySelector("body")
    .setAttribute(
      "style",
      `height:${viewHeight}px; max-height:${viewHeight}px;`
    );
};
