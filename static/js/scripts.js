document.addEventListener('DOMContentLoaded', function () {
    const filterBtn = document.querySelector('.filter-btn');
    const filterMenu = document.querySelector('.filter-menu');

    filterBtn.addEventListener('click', function () {
        filterMenu.classList.toggle('active');
    });

    // Скрываем меню при клике вне области меню и кнопки
    document.addEventListener('click', function (event) {
        if (!filterBtn.contains(event.target) && !filterMenu.contains(event.target)) {
            filterMenu.classList.remove('active');
        }
    });
});
