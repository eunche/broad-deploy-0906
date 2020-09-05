let commentPK = "down";

function addRecoment(event) {
  if (event.target.classList.contains("jsAddtargeting")) {
    const targetButton = event.target;
    const submitBox = document.querySelector("#id_body");
    const commentForm = document.querySelector(".post-form");
    targetButton.classList.remove("jsAddtargeting");
    targetButton.innerText = "답글 쓰기";
    submitBox.classList.remove("set_border_brown");
    addedPk = document.querySelector(".jsAddedPk");
    addedPk.remove();
    commentPK = "down";
  } else {
    if (commentPK != "down") {
      return;
    }
    const targetButton = event.target;
    const submitBox = document.querySelector("#id_body");
    const commentForm = document.querySelector(".post-form");
    commentPK = event.target.classList.item(1);
    targetButton.classList.add("jsAddtargeting");
    targetButton.innerText = "답글중";
    submitBox.classList.add("set_border_brown");
    commentForm.insertAdjacentHTML(
      "beforeend",
      `
    <input class="jsAddedPk" type="hidden" name="pk" value="${commentPK}">
    `
    );
  }
}
