// Function to update grid items based on panels from JSON
function updateGridItems() {
    var gridItems = document.querySelectorAll('.grid-item');
    pages.forEach(function (page) {
        page.panels.forEach(function (panel, index) {
            var gridItem = gridItems[index];
            gridItem.style.display = 'block'; // Display the grid item
            gridItem.style.gridRow = 'span ' + panel.row_span;
            gridItem.style.gridColumn = 'span ' + panel.col_span;
            gridItem.innerText = panel.image; // Set inner text for demonstration
        });
        // Hide remaining grid items if not enough panels
        for (var i = page.panels.length; i < gridItems.length; i++) {
            gridItems[i].style.display = 'none';
        }
    });
}

// Call the function to place dialogs when the DOM content is loaded
document.addEventListener('DOMContentLoaded',  updateGridItems() );

