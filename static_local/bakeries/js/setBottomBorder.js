const setBottomBorder = () => {
  const beforeURL = document.referrer;
  if (beforeURL.includes("like")) {
    document
      .querySelector(".bottom_icons")
      .children.item(3)
      .classList.add("set_bottom_black");
  } else {
    document
      .querySelector(".bottom_icons")
      .children.item(2)
      .classList.add("set_bottom_black");
  }
};

setBottomBorder();
