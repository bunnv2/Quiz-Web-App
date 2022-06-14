homeItem =  document.getElementById("homeItem");
quizesItem =  document.getElementById("quizesItem");
createItem =  document.getElementById("creatorItem");
signItem =  document.getElementById("signItem");

items = [homeItem, quizesItem, createItem, signItem];
activeURL = window.location.pathname;

function changeActiveItem(item) {
    for (var i = 0; i < items.length; i++) {
        item.classList.add("active");
        if (items[i] != item) {
            items[i].classList.remove("active");
        }
    }
    item.classList.add("active");
}
if (activeURL == "/") {
    changeActiveItem(homeItem);
}
else if (activeURL.includes("quiz/create")) {
    changeActiveItem(createItem);
}
else if (activeURL.includes("quiz/quizes")) {
    changeActiveItem(quizesItem);
}
else if (activeURL.includes("/sign")) {
    changeActiveItem(signItem);
}

