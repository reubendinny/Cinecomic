path = '../frames/final/'
current_page = 0

function placeDialogs(page) {
    var gridItems = document.querySelectorAll('.grid-item');
    page.panels.forEach(function (panel, index) {
        var gridItem = gridItems[index];
        // gridItem.style.display = 'block'; // Display the grid item
        gridItem.style.gridRow = 'span ' + panel.row_span;
        gridItem.style.gridColumn = 'span ' + panel.col_span;
        gridItem.style.backgroundImage = `url("${path}${panel.image}.png")`;

        gridItem.innerHTML = "";

        const bubble_temp = document.createElement('div');
        bubble_temp.classList.add('bubble');
        bubble_temp.style.position = 'relative';
        bubble_temp.innerHTML = page['bubbles'][index]['dialog'];

        // bubble_temp.style.transform = `translate(${page['bubbles'][index]['bubble_offset_x']}px, ${page['bubbles'][index]['bubble_offset_y']}px)`
        bubble_temp.style.transform = `translate(0px, 0px)`
        console.log(bubble_temp.style.transform )
    
        const tail= document.createElement('div'); // Create a new div for the tail
        tail.classList.add('tail'); // Add the 'tail' class to the div
        tail.style.transform = `translate(${page['bubbles'][index]['tail_offset_x']}px, ${page['bubbles'][index]['tail_offset_y']}px) rotate(${page['bubbles'][index]['tail_deg']}deg)`
        bubble_temp.appendChild(tail);


        gridItem.appendChild(bubble_temp);
    });

    // Hide remaining grid items if not enough panels
    for (var i = page.panels.length; i < gridItems.length; i++) {
        gridItems[i].style.display = 'none';
    }
}

// Call the function to place dialogs when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    placeDialogs(pages[current_page]);
});

function prevPage(){
    current_page = (current_page - 1);
    placeDialogs(pages[current_page]);
}

function nextPage(){
    current_page = (current_page + 1) % pages.length;
    console.log(current_page)
    placeDialogs(pages[current_page]);
}

