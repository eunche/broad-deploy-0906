const listElement = document.querySelector(".list");
const scon = document.querySelector(".jsScon");
const cake = document.querySelector(".jsCake");
const makarong = document.querySelector(".jsMakarong");
const croffle = document.querySelector(".jsCroffle");
const tart = document.querySelector(".jsTart");
let pickedData;

const listInfoHTML = (
  pk,
  index,
  name,
  subName,
  address,
  totalRating,
  reviewCount
) => {
  return `
<a href="/bakery/${pk}" class="list_store">
  <div class="store_rank">${index}</div>
  <div class="store_detail">
      <div class="detail_top">
          <span class="top_name">${name}</span>
      </div>
      <div class="detail_explain">${subName.substr(0, 25)}</div>
      <div class="detail_address">${address}</div>
  </div>
  <div class="store_review">
      <div class="review_score">
          <span class="score_star">★</span>
          <span class="score_number">${
            totalRating != 0 ? totalRating.toFixed(1) : "&nbsp;&nbsp;-"
          }</span>
      </div>
      <div class="review_number">
          <span class="review_count">리뷰 ${reviewCount}</span>
      </div>
  </div>
</a>
`;
};

const addInfo = (JSONData) => {
  let temp;
  const listStoreElement = document.querySelectorAll(".list_store");
  for (const i of listStoreElement) {
    i.remove();
  }
  for (let i in JSONData) {
    if (temp != JSONData[i].fields.name) {
      listElement.insertAdjacentHTML(
        "beforeend",
        listInfoHTML(
          JSONData[i].pk,
          parseInt(i) + 1,
          JSONData[i].fields.name,
          JSONData[i].fields.sub_name,
          JSONData[i].fields.address,
          JSONData[i].fields.temp_total_rating,
          JSONData[i].fields.temp_review_count
        )
      );
      temp = JSONData[i].fields.name;
    }
  }
};

const clickCategory = async (event) => {
  let eng_bread;
  let breadElementList = [scon, cake, makarong, croffle, tart];
  let breadList = ["스콘", "케이크", "마카롱", "크로플", "타르트"];
  let bread = event.target.parentElement.querySelector(".menu_1__name")
    .innerText;
  if (bread === breadList[0]) {
    eng_bread = "scon";
  } else if (bread === breadList[1]) {
    eng_bread = "cake";
  } else if (bread === breadList[2]) {
    eng_bread = "makarong";
  } else if (bread === breadList[3]) {
    eng_bread = "croffle";
  } else if (bread === breadList[4]) {
    eng_bread = "tart";
  }
  let breadIndex = breadList.indexOf(bread);
  if (breadIndex != 0) {
    let temp;
    temp = breadElementList[0];
    breadElementList[0] = breadElementList[breadIndex];
    breadElementList[breadIndex] = temp;
  }
  if (breadElementList[0].classList.contains("opacity_1")) {
  } else {
    breadElementList[0].classList.add("opacity_1");
    for (let index = 1; index < breadElementList.length; index++) {
      breadElementList[index].classList.remove("opacity_1");
    }
  }
  try {
    const get = await $.getJSON(
      `https://${awsURL}/bakery/${eng_bread}-data/`,
      (data) => {
        pickedData = data;
      }
    );
    const setting = await addInfo(pickedData);
  } catch {
  } finally {
  }
};

$.getJSON(`https://${awsURL}/bakery/tart-data/`, (data) => {
  addInfo(data);
});
