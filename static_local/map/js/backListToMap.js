const backListToMap = () => {
  newContent.remove();
  content.classList.remove("set_none");
  header.innerHTML = beforeHeader;
  document.querySelector("body").classList.remove("overflow_none");
  content.insertAdjacentHTML(
    "afterbegin",
    `
    <div class="scroll_available"></div>
  `
  );
  let scrollAvailable = document.querySelector(".scroll_available");
  scrollAvailable.addEventListener("touchend", touchScrollAvailable, false);
};
