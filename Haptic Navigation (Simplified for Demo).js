let isDragging = false;
let lastX = 0;

globeCanvas.addEventListener("mousedown", e => {
  isDragging = true;
  lastX = e.clientX;
});

window.addEventListener("mouseup", () => isDragging = false);

window.addEventListener("mousemove", e => {
  if (!isDragging) return;
  const delta = e.clientX - lastX;
  lastX = e.clientX;
  rotateGlobe(delta * 0.005); // sensitivity
});
