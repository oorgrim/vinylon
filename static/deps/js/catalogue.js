document.addEventListener('DOMContentLoaded', function() {
    sessionStorage.clear();
    localStorage.clear();
    console.log("cleared");
    // for(let i=0; i<localStorage.length; i++) {
    //     let key = localStorage.key(i);
    //     alert(`${key}: ${localStorage.getItem(key)}`);
    // }
});


let searchTagList = document.getElementsByClassName("searchTag");
console.log(1)
for (let i = 0; i < searchTagList.length; i++) {
    searchTagList[i].addEventListener('click', () => {
        buttonClick(searchTagList[i]);
    });
}


function addToStorage(tagQuery, tagList){
    for(let i = 0; i < tagList.length; i++){
        if(tagQuery == tagList[i].value){
            localStorage.setItem(`${tagQuery}`, tagQuery);              
        }
    }
}

function removeFromStorage(tagQuery, tagList){
    for(let i = 0; i < tagList.length; i++){
        if(tagQuery == tagList[i].value){
            localStorage.removeItem(tagQuery);              
        }
    }
}

function filterVinyls(vinylList, appliedTags){
    let keyList = [];
    for(let i = 0; i < localStorage.length; i++) {
        let key = localStorage.key(i);
        keyList.push(key);
    }
    if(keyList.length == 0){
        for(let i = 0; i < vinylList.length; i++){
            vinylList[i].setAttribute("style", "display: block;");
        }
    }
    else{
        for(let i = 0; i < vinylList.length; i++){
            vinylList[i].setAttribute("style", "display: none;");
        }
        for(let i = 0; i < vinylList.length; i++){
            for(let j = 0; j < appliedTags[i].children.length; j++){
                if(keyList.includes(appliedTags[i].children[j].innerText)){
                    console.log(vinylList[i].children[2].innerText + ':' + appliedTags[i].children[j].innerText);
                    vinylList[i].setAttribute("style", "display: block;");
                }
                
            }
            
        }
    }
}

function buttonClick(button) {
    tagName = button.value;
    let tagList = document.getElementsByClassName("searchTag")
    let vinylList = document.getElementsByClassName("vinyl_record")
    let appliedTags = document.getElementsByClassName("vinyl_tags")

    if (button.style.backgroundColor == 'rgb(142, 191, 186)') {
        button.style.backgroundColor = 'black';
        button.style.color = 'white';
        removeFromStorage(tagName, tagList);
    } 
    else {
        button.style.backgroundColor = 'rgb(142, 191, 186)';
        button.style.color = 'black';
        addToStorage(tagName, tagList);
    }
    filterVinyls(vinylList, appliedTags);
}
