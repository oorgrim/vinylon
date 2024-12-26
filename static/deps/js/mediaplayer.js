window.onload = function () {
    const audioPlayer = document.getElementById("audio-player");
    const audioSource = document.getElementById("audio-source");
    const nowPlaying = document.getElementById("current-track");

    // ф-ия для воспроизв трека
    window.playAudio = function (element) {
        const audioSrc = element.dataset.src;
        const audioTitle = element.querySelector(".audio-title").innerText;

        //  новый источник аудио
        audioSource.src = audioSrc;
        audioPlayer.load();
        audioPlayer.play();

        // обновая отображения текущего трека
        nowPlaying.innerText = audioTitle;

        // сбросить стили для всех треков
        const allItems = document.querySelectorAll(".audio-item");
        allItems.forEach(item => item.classList.remove("playing"));

        element.classList.add("playing");
    };
};
