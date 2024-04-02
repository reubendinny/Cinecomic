function placeDialogs() {
    var i = 0;
    const gridItems = document.querySelectorAll('.grid-item'); // Select all grid items

    gridItems.forEach(item => {
        const dialog= document.createElement('div'); // Create a new div for dialog
        dialog.classList.add('dialog'); // Add the 'dialog' class to the div
        dialog.style.transform = "translate(45px, 45px)"
       
        dialog.innerHTML = bubble[i]['dialog']; // Add content to the dialog
        i = i +1;   
        const tail= document.createElement('div'); // Create a new div for the tail
        tail.classList.add('tail'); // Add the 'tail' class to the div
        dialog.appendChild(tail); // Append the tail div to the dialog div
        tail.style.transform = `translate(45px, 45px) rotate(${bubble[i]['tail_deg']}deg)`


        item.appendChild(dialog); // Append the dialog div to the current grid item
    });
}

// Call the function to place dialogs when the DOM content is loaded
document.addEventListener('DOMContentLoaded', placeDialogs);


