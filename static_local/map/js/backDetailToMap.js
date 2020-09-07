const backDetailToMap = () => {
  detailContent.remove();
  content.classList.remove("set_none");
  document.querySelector("body").classList.remove("overflow_none");
  document.querySelector("header").innerHTML = mapHeader;
  content.insertAdjacentHTML(
    "afterbegin",
    `
    <div class="scroll_available"></div>
  `
  );
  let scrollAvailable = document.querySelector(".scroll_available");
  scrollAvailable.addEventListener("touchend", touchScrollAvailable, false);
};
