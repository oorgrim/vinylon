audios = document.getElementsByTagName("source");  

window.onload = function(){
    for(let i = 0; i < audios.length; i++){
        audios[i].parentElement.setAttribute('style', 'display:none');
    }

    ulList = document.getElementsByTagName("ul");
    for(let i = 0; i < ulList.length; i++){
        if(ulList[i].children.length <= 1){
            ulList[i].setAttribute('style', 'display:none;');
        }
        else{
            ulList[i].setAttribute('style', 'display:block;');
        }
    }
}

function sendValue(song){
    mediaUrl = song.dataset["dir"] + "\\media\\";
    console.log(mediaUrl);
    songContainers = document.getElementsByClassName("song");
    for(let i = 0; i < songContainers.length; i++){
        songContainers[i].setAttribute('style', 'color:black');
    }
    song.setAttribute('style', 'color:blue');
    for(let i = 0; i < audios.length; i++){
        console.log(mediaUrl + song.children[1].innerHTML);
        console.log(audios[i].src);
        if(mediaUrl + song.children[1].innerHTML == audios[i].src){
            audios[i].parentElement.setAttribute('style', 'display:block');
            console.log(audios[i].src);
        }
        else{
            audios[i].parentElement.setAttribute('style', 'display:none');
        }
    }            
}