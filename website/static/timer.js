function startTimer(display) {
  var startTime = Date.now();

  setInterval(function () {
    var elapsedTime = Date.now() - startTime;
    var seconds = Math.floor(elapsedTime / 1000);
    var minutes = Math.floor(seconds / 60);
    seconds %= 60;
    minutes %= 60;

    var displayText = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
    display.textContent = displayText;
  }, 1000);
}

window.onload = function () {
  var display = document.querySelector("#timer");
  startTimer(display);
};

// use <div id="timer">0:00</div> to display the timer in html
