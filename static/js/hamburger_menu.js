document.addEventListener('DOMContentLoaded', function() {
  function toggleMenu() {
    var menu = document.getElementById("hamburger-menu");
    if (menu.classList.contains("open")) {
      menu.classList.remove("open");
    } else {
      menu.classList.add("open");
    }
  }
  document.querySelector('.navbar-toggler').addEventListener('click', toggleMenu);
});
