document.addEventListener("DOMContentLoaded", function() {
    const lens = document.getElementById('lens');
    const object = document.getElementById('object');
    const image = document.getElementById('image');

    let focalLength = 100; // Set the focal length of the lens

    function updateImagePosition() {
        let objectDistance = parseFloat(object.style.left) - parseFloat(lens.style.left);
        let imageDistance = 1 / ((1 / focalLength) - (1 / objectDistance));

        image.style.left = `${parseFloat(lens.style.left) + imageDistance}px`;
    }

    object.addEventListener('drag', function(event) {
        object.style.left = `${event.clientX}px`;
        updateImagePosition();
    });

    // Initial positioning
    object.style.left = '200px';
    updateImagePosition();
});
