let index = 0;
slideShow();

function slideShow() {
    // Grab all image containers
    let slides = document.querySelectorAll(".slideshow");

    // Remove display for all of them
    slides.forEach(slide => slide.style.display= "none");

    // Increase index variable by 1 and then check if index value is higher than slides array length
    // If it is reset index value to 1, in order to restart the loop from first image
    index++;
    if (index > slides.length) {
        index = 1;
    }

    // Display slide iteration equalling the index value -1
    // -1 because the array index is zero-based
    slides[index -1].style.display = "block";

    // Call the slideShow function every 5 seconds
    setTimeout(slideShow, 5000);
}
