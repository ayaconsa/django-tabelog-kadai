document.addEventListener('DOMContentLoaded', function() {
  function toggleMenu() {
    var menu = document.getElementById("hamburger_menu");
    if (menu.classList.contains("open")) {
      menu.classList.remove("open");
    } else {
      menu.classList.add("open");
    }
  }

  document.querySelector('.navbar_toggler').addEventListener('click', toggleMenu);
  document.querySelector('.close_btn').addEventListener('click', toggleMenu);
});
