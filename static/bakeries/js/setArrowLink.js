const setArrowLink = () => {
  const beforeURL = document.referrer;
  if (beforeURL.includes("reviews")) {
    history.go(-2);
  } else if (beforeURL.includes("broad")) {
    history.go(-1);
  } else {
    location.href = `http://${awsURL}`;
  }
};
