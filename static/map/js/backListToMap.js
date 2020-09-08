const backListToMap = () => {
  isReturn = true;
  newContent.remove();
  document.querySelector(".header_blank").insertAdjacentHTML(
    "afterend",
    `
    <div class="content"></div>
    `
  );
  content = document.querySelector(".content");
  content.innerHTML = contentHTML;
  delete map;
  delete polygon;
  for (let i in markers) {
    markers[i].setMap(null);
  }
  container = document.getElementById("map"); //새로생긴 div map의 DOM
  polygonPath = [];
  polygon.setMap(null);
  try {
    clusterer.removeMarkers(markers);
  } catch (error) {}
  markers = [];
  startMap();
  document.querySelector("body").classList.remove("overflow_none");
  header.innerHTML = beforeHeader;
};
