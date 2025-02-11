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