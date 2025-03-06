document.addEventListener('DOMContentLoaded', function() {
    sessionStorage.clear();
});

let searchTagList = document.getElementsByClassName("searchTag");
for (let i = 0; i < searchTagList.length; i++) {
    searchTagList[i].addEventListener('click', () => {
        buttonClick(searchTagList[i]);
    });
}

function addToStorage(tagQuery, tagList) {
    for (let i = 0; i < tagList.length; i++) {
        if (tagQuery === tagList[i].value) {
            localStorage.setItem(tagQuery, tagQuery);
        }
    }
}

function removeFromStorage(tagQuery, tagList) {
    for (let i = 0; i < tagList.length; i++) {
        if (tagQuery === tagList[i].value) {
            localStorage.removeItem(tagQuery);
        }
    }
}

function filterVinyls(vinylList, appliedTags) {
    let keyList = [];
    
    for (let i = 0; i < localStorage.length; i++) {
        let key = localStorage.key(i);
        keyList.push(key);
    }
    
    keyList = keyList.filter(key => key !== "djdt.show");

    let keySet = new Set(keyList);

    if (keySet.size === 0) {
        for (let i = 0; i < vinylList.length; i++) {
            vinylList[i].style.display = "block";
        }
    } else {
        for (let i = 0; i < vinylList.length; i++) {
            let hasMatch = [...appliedTags[i].children].some(tag => keySet.has(tag.innerText));
            vinylList[i].style.display = hasMatch ? "block" : "none";
        }
    }
}

function buttonClick(button) {
    let tagName = button.value;
    let tagList = document.getElementsByClassName("searchTag");
    let vinylList = document.getElementsByClassName("vinyl_record");
    let appliedTags = document.getElementsByClassName("vinyl_tags");

    button.classList.toggle("selected");

    if (button.classList.contains("selected")) {
        addToStorage(tagName, tagList);
    } else {
        removeFromStorage(tagName, tagList);
    }

    filterVinyls(vinylList, appliedTags);
}
