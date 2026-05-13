document.querySelectorAll(".panel").forEach(panel => {
  panel.addEventListener("click", () => {
    setCinemaWorld(panel.id);
  });
});
