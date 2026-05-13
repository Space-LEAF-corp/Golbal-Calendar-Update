let ambient = new Audio("ambient.mp3");
ambient.loop = true;

ambientToggle.addEventListener("click", () => {
  if (ambient.paused) ambient.play();
  else ambient.pause();
});
