const updates = [
  "NASA reports clear skies for upcoming launch.",
  "New coral reef discovered in protected waters.",
  "International robotics teams celebrate youth innovation awards."
];

let index = 0;
setInterval(() => {
  newsText.textContent = updates[index % updates.length];
  index++;
}, 10000);
