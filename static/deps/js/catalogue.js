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

function filterVinyls(vinylList){
    let keyList = [];
    for(let i = 0; i < localStorage.length; i++) {
        let key = localStorage.key(i);
        keyList.push(key)
    }
    for(let j = 0; j < vinylList.length; j++){
        if(keyList.includes(vinylList[j])){
            console.log(key)
            vinylList[j].setAttribute("style", "display: block;");
        }
        else{
            vinylList[j].setAttribute("style", "display: none;");
        }
    }
}

function buttonClick(button) {
    tagName = button.value;
    let tagList = document.getElementsByClassName("searchTag")
    let vinylList = document.getElementsByClassName("vinyl_record")

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
    filterVinyls(vinylList);
}


$(document).ready(function() {
// тут прверка нажатия и удаление
$('#test').click(function() {
    alert('Button clicked!');
});

$(document).on('click', '.delete-vinyl', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "cart:cart_delete" %}',
        data: {
            vinyl_id: $(this).data('index'),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },
        success: function(json) {
            location.reload();
        },
        error: function(xhr, errmsg, err) {
            console.error(xhr.status + ": " + xhr.responseText);
        }
    });
});
});