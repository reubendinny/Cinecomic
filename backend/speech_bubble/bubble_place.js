function placeDialogs() {
    var i = 1;
    const gridItems = document.querySelectorAll('.grid-item'); // Select all grid items

    gridItems.forEach(item => {
        const dialog= document.createElement('div'); // Create a new div for dialog
        dialog.classList.add('dialog'); // Add the 'dialog' class to the div
        dialog.id = `dialog_${i}`;

        const tail= document.createElement('div'); // Create a new div for the tail
        tail.classList.add('tail'); // Add the 'tail' class to the div
        tail.id = `tail${i}`;

        dialog.appendChild(tail); // Append the tail div to the dialog div
        item.appendChild(dialog); // Append the dialog div to the current grid item

        i++;

    });
    updateDialogs(1)

}

// Call the function to place dialogs when the DOM content is loaded
document.addEventListener('DOMContentLoaded', placeDialogs);


function updateDialogs(start){
    var i = 1;
    var count = 0;
    
    for(j=0;j<start-1;j++){
        count = count + (page_template[j]).length
    }
        
    console.log(count)

    

    const gridItems = document.querySelectorAll('.grid-item'); // Select all grid items



    gridItems.forEach(item => {
        const dialog_temp = document.getElementById(`dialog_${i}`); // Create a new div for dialog
        console.log(dialog_temp)
        dialog_temp.style.transform = "translate(45px, 45px)"
       
        dialog_temp.innerHTML = bubble[count + i]['dialog']; // Add content to the dialog
        console.log(i)

        // const tail_temp= document.getElementById(`tail${i}`) // Create a new div for the tail
        // tail_temp.style.transform = `translate(45px, 45px) rotate(${bubble[i]['tail_deg']}deg)`
        
        i++;

    });


}





function nextPage() {
    const page = document.getElementById("pageStyle")
    const hrefValue = page.getAttribute("href");
    console.log("Href value:", hrefValue);


    var match = hrefValue.match(/\d+/);

    // Check if there is a match
    if (match) {
        var integerValue = parseInt(match[0]); // Convert matched string to integer
        integerValue++; // Increment the integer value
        var updatedCssFilePath = hrefValue.replace(/\d+/, integerValue); // Update the integer in the string
        page.setAttribute("href", updatedCssFilePath)
        // console.log(updatedCssFilePath)
        // count = count+(page_template[count-1]).length

    } else {
        console.log("No integer found in the string");
    }

    updateDialogs(integerValue)
}

function prevPage() {
    const page = document.getElementById("pageStyle")
    const hrefValue = page.getAttribute("href");
    console.log("Href value:", hrefValue);


    var match = hrefValue.match(/\d+/);

    // Check if there is a match
    if (match) {
        var integerValue = parseInt(match[0]); // Convert matched string to integer
        integerValue--; // Increment the integer value
        var updatedCssFilePath = hrefValue.replace(/\d+/, integerValue); // Update the integer in the string
        page.setAttribute("href", updatedCssFilePath)
        // console.log(updatedCssFilePath)

    } else {
        console.log("No integer found in the string");
    }


}