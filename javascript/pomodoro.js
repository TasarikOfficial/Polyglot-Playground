const minutes = Number(process.argv[2] || 25);
let seconds = minutes * 60;
console.log(`Focus session started: ${minutes} min`);
const timer = setInterval(() => {
  const m = String(Math.floor(seconds / 60)).padStart(2, "0");
  const s = String(seconds % 60).padStart(2, "0");
  process.stdout.write(`\r🍅 ${m}:${s}`);
  if (seconds-- === 0) {
    clearInterval(timer);
    console.log("\nDone. Take a mindful break.");
  }
}, 1000);
