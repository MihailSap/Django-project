function toggleSidebar() {
    const sidebar = document.querySelector('aside');
    const main = document.querySelector('main');
    sidebar.classList.toggle('hidden');
    main.classList.toggle('collapsed');
}