function sendValue(audioUrl) {
    let audioPlayer = document.getElementById("audio-player");
    let audioSource = document.getElementById("audio-source");

    audioSource.src = `/media/${audioUrl}`;
    audioPlayer.load();
    audioPlayer.play();
}
