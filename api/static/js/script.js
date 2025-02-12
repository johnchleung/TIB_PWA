let isLayout1 = true;

function toggleLayout() {
    const container = document.getElementById('layoutContainer');
    if (isLayout1) {
        container.classList.remove('layout-1');
        container.classList.add('layout-2');
    } else {
        container.classList.remove('layout-2');
        container.classList.add('layout-1');
    }
    isLayout1 = !isLayout1; // Toggle the layout state
}

function toggleGreyscale() {
    const sections = [document.querySelector('.section2'), 
                      document.querySelector('.section3'), 
                      document.querySelector('.section4')];
    sections.forEach(section => {
        if (section.style.filter === 'grayscale(100%)') {
            section.style.filter = 'none';
        } else {
            section.style.filter = 'grayscale(100%)';
        }
    });
}