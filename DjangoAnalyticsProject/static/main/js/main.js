function toggleSidebar() {
    const sidebar = document.querySelector('aside');
    const main = document.querySelector('main');
    sidebar.classList.toggle('hidden');
    main.classList.toggle('collapsed');
}

function toggleMenu() {
    const menu = document.getElementById('dropdown-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

document.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdown-menu');
    const username = document.querySelector('.username');

    if (!dropdown.contains(event.target) && !username.contains(event.target)) {
        dropdown.style.display = 'none';
    }
});

window.addEventListener('scroll', function () {
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');
    if (window.scrollY > 300) {
        scrollToTopBtn.classList.add('show');
    } else {
        scrollToTopBtn.classList.remove('show');
    }
});

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}
