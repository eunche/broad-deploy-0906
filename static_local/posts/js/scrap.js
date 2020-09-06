const changeScrapDB = () => {
  $.ajax({
    type: "POST",
    url: ajaxScrapUrl,
    data: { pk: postPK, csrfmiddlewaretoken: csrf },
    dataType: "json",
  });
};

const clickScrap = () => {
  const scrap = document.querySelector(".jsScrap");
  const scrapImg = document.querySelector(".jsScrapImg");
  const scrapText = document.querySelector(".jsScraptext");
  if (scrapImg.src === `/static/posts/img/star.png`) {
    scrapImg.src = `/static/posts/img/white_star.png`;
    scrapText.classList.remove("text-color-gold");
    scrap.classList.remove("border-color-gold");
  } else {
    scrapImg.src = `/static/posts/img/star.png`;
    scrapText.classList.add("text-color-gold");
    scrap.classList.add("border-color-gold");
  }
  changeScrapDB();
};
