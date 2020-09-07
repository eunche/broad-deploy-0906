const changeLikeDB = () => {
  $.ajax({
    type: "POST",
    url: ajaxLikeUrl,
    data: { pk: bakeryPK, csrfmiddlewaretoken: csrf },
    dataType: "json",
  });
};

const clickLike = () => {
  let like = document.querySelector(".jsLike");
  if (like.src === `http://${awsURL}/static/bakeries/img/heart.png`) {
    like.src = `http://${awsURL}/static/bakeries/img/white_heart.png`;
  } else {
    like.src = `http://${awsURL}/static/bakeries/img/heart.png`;
  }
  changeLikeDB();
};
