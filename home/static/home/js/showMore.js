function toggleText() {
    // Get all the elements from the page
    let dots = document.getElementById("dots");
    let moreText = document.getElementById("more-text");
    let buttonText = document.getElementById("text-button");
  
    // If the display property of the dots to be displayed is already set to 'none' (that is hidden) then this 
    // section of code triggers
    if (dots.style.display === "none") {
        // Show the dots after the text
        dots.style.display = "inline";

        // Hide the text between the span elements
        moreText.style.display = "none";

        // Change the text on button to 'Show More' and the icon to caret down
        buttonText.innerHTML = "<span class='icon'><i class='fas fa-caret-down'></i></span><span class='text-uppercase'>Show More</span>";
    }

    // If the hidden portion is revealed, we will change it back to be hidden
    else {
        // Hide the dots after the text
        dots.style.display = "none";
        
        // Show the text between the span elements
        moreText.style.display = "inline";

        // Change the text on button to 'Show Less' and the icon to caret up
        buttonText.innerHTML = "<span class='icon'><i class='fas fa-caret-up'></i></span><span class='text-uppercase'>Show Less</span>";
    }
}