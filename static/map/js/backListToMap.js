const backListToMap = () => {
  newContent.remove();
  content.classList.remove("set_none");
  header.innerHTML = beforeHeader;
  document
    .querySelector("#map")
    .setAttribute("style", `height:${viewHeight}px;`);
};
