const button = document.getElementById("theme");
let dark = false;
try {
  dark = localStorage.getItem("sitong-theme") === "dark";
} catch {}
function applyTheme() {
  document.body.classList.toggle("dark", dark);
  button.setAttribute("aria-pressed", String(dark));
}
applyTheme();
button.addEventListener("click", () => {
  dark = !dark;
  applyTheme();
  try {
    localStorage.setItem("sitong-theme", dark ? "dark" : "light");
  } catch {}
});
