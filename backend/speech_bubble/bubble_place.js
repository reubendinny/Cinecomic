function placeDialogs() {
    const gridItems = document.querySelectorAll('.grid-item'); // Select all grid items

    gridItems.forEach(item => {
        const dialog= document.createElement('div'); // Create a new div for dialog
        dialog.classList.add('dialog'); // Add the 'dialog' class to the div
        dialog.style.transform = "translate(45px, 45px)"
       
        dialog.innerHTML = 'Hello, this is testing. Will this work?'; // Add content to the dialog

        const tail= document.createElement('div'); // Create a new div for the tail
        tail.classList.add('tail'); // Add the 'tail' class to the div
        dialog.appendChild(tail); // Append the tail div to the dialog div
        tail.style.transform = "translate(45px, 45px) rotate(0deg)"


        item.appendChild(dialog); // Append the dialog div to the current grid item
    });
}

// Call the function to place dialogs when the DOM content is loaded
document.addEventListener('DOMContentLoaded', placeDialogs);


