const renderDropdown = (node: Element) => {
    console.log({ node });
    const listItems = node.querySelectorAll('li');

    const h = document.location.href;
    listItems.forEach((listItem) => {
        const a = listItem.querySelector('a');
        listItem.classList.toggle('active', a.href === h);
    });
};

export const initDropdown = () =>
    window.addEventListener('load', () => {
        const dropdowns = document.querySelectorAll('.translations .dropdown');
        dropdowns.forEach(renderDropdown);
    });
