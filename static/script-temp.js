const carousel = document.querySelector('.carousel');
const carouselItems = carousel.querySelectorAll('.carousel-item');
let currentItem = 0;

function changeImage() {
  carouselItems.forEach((item, index) => {
    if (index === currentItem) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });
  currentItem = (currentItem + 1) % carouselItems.length;
}

setInterval(changeImage, 3000);

const box = document.querySelector('.box');

setTimeout(() => {
    box.classList.add('visible');
}, 2000);


var selectedFile = null;
var selectedLink = '';
var linkInputVisible = false;

function openFilePicker() {
    // Hide the link input when "Upload Video" button is clicked
    hideLinkInput();
  
    // Trigger click event on the file input element
    document.getElementById('fileInput').click();
}

document.getElementById('fileInput').addEventListener('change', function() {
    // Get the selected file
    selectedFile = this.files[0];
  
    // Display the file name
    document.getElementById('fileName').textContent = 'Selected File: ' + selectedFile.name;
});

function toggleLinkInput() {
    var linkInputContainer = document.getElementById('linkInputContainer');
    linkInputVisible = !linkInputVisible;
    if (linkInputVisible) {
        linkInputContainer.style.display = 'block';
    } else {
        linkInputContainer.style.display = 'none';
        // Clear link input when hiding
        document.getElementById('link-input').value = '';
        selectedLink = '';
    }
}

function hideLinkInput() {
    document.getElementById('linkInputContainer').style.display = 'none';
    // Clear link input when hiding
    document.getElementById('link-input').value = '';
    selectedLink = '';
}

document.getElementById('link-input').addEventListener('input', function() {
    // Get the entered link
    selectedLink = this.value;

    // Clear file input
    selectedFile = null;

    // Clear file name display
    document.getElementById('fileName').textContent = '';
});

function submitForm() {
    if (selectedFile !== null && selectedLink === '') {
        document.getElementById('submissionResult').textContent = selectedFile.name;
    } else if (selectedLink !== '' && selectedFile === null) {
        document.getElementById('submissionResult').textContent = Submitted;
    } else {
        document.getElementById('submissionResult').textContent = 'Please select either a file or enter a link.';
    }
    // document.getElementById('submissionResult').textContent = 'Submitted';
}

// var selectedFile = null;
// var selectedLink = '';
// var linkInputVisible = false;

// document.getElementById('fileInput').addEventListener('change', function() {
//     // Get the selected file
//     selectedFile = this.files[0];
  
//     // Display the file name
//     document.getElementById('fileName').textContent = 'Selected File: ' + selectedFile.name;
// });

// function toggleLinkInput() {
//     var linkInputContainer = document.getElementById('linkInputContainer');
//     linkInputVisible = !linkInputVisible;
//     if (linkInputVisible) {
//         linkInputContainer.style.display = 'block';
//     } else {
//         linkInputContainer.style.display = 'none';
//         // Clear link input when hiding
//         document.getElementById('link-input').value = '';
//         selectedLink = '';
//     }
// }

// document.getElementById('link-input').addEventListener('input', function() {
//     // Get the entered link
//     selectedLink = this.value;

//     // Clear file input
//     selectedFile = null;

//     // Clear file name display
//     document.getElementById('fileName').textContent = '';
// });

// function submitForm() {
//     if (selectedFile !== null && selectedLink === '') {
//         document.getElementById('submissionResult').textContent = 'Submitted';
//     } else if (selectedLink !== '' && selectedFile === null) {
//         document.getElementById('submissionResult').textContent = 'Submitted';
//     } else {
//         document.getElementById('submissionResult').textContent = 'Please select either a file or enter a link.';
//     }
// }
