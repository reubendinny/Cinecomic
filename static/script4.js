// 1. Background image carousel
const carousel = document.querySelector('.carousel');
const carouselItems = carousel.querySelectorAll('.carousel-item');
const submissionResult = document.getElementById('submissionResult')
const linkInput = document.getElementById('link-input')

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

// 2. Box with title, description and (file uploader/link & submit button)
const box = document.querySelector('.box');
setTimeout(() => {
    box.classList.add('visible');
}, 2000);


var selectedFile = null;
var selectedLink = '';
var linkInputVisible = false;

// 3. File uploader
function openFilePicker() {
    hideLinkInput();
    document.getElementById('fileInput').click();
}

document.getElementById('fileInput').addEventListener('change', function() {
    selectedFile = this.files[0];
    document.getElementById('fileName').textContent = 'Selected File: ' + selectedFile.name;
    hideLinkInput(); // Hide link input if file is selected
    showVideoPreview(URL.createObjectURL(selectedFile)); // Show video preview
});

// document.getElementById('fileInput').addEventListener('change', function() {
//     selectedFile = this.files[0];
//     document.getElementById('fileName').textContent = 'Selected File: ' + selectedFile.name;
// });

//4. Link
function toggleLinkInput() {
    var linkInputContainer = document.getElementById('linkInputContainer');
    linkInputVisible = !linkInputVisible;
    if (linkInputVisible) {
        linkInputContainer.style.display = 'block';
    } else {
        linkInputContainer.style.display = 'none';
        document.getElementById('link-input').value = '';
        selectedLink = '';
    }
}

function hideLinkInput() {
    document.getElementById('linkInputContainer').style.display = 'none';
    document.getElementById('link-input').value = '';
    selectedLink = '';
}

document.getElementById('link-input').addEventListener('input', function() {
    selectedLink = this.value;
    selectedFile = null;
    document.getElementById('fileName').textContent = '';
    hideVideoPreview(); // Hide video preview if link is entered
});

//5. Submit button
function submitForm() {
    // If file is selected
    if (selectedFile !== null && selectedLink === '') {
        submissionResult.textContent = "Your comic is being created";
        var formdata = new FormData();
        formdata.append("file", selectedFile);

        var requestOptions = {
          method: "POST",
          body: formdata,
          redirect: "follow",
        };

        fetch("/uploader", requestOptions)
          .then((response) => response.text())
          .then((result) => {
            console.log(result);
            submissionResult.textContent = result;
          })
          .catch((error) => {
            console.log("error", error);
            alert(error);
          });
          
    } 
    
    // If link is entered
    else if (selectedLink !== '' && selectedFile === null) {
        submissionResult.textContent = "Your comic is being created";

        var formdata = new FormData();
        formdata.append("link", linkInput.value);

        var requestOptions = {
          method: "POST",
          body: formdata,
          redirect: "follow",
        };

        fetch("/handle_link", requestOptions)
          .then((response) => response.text())
          .then((result) => {
            console.log(result);
            submissionResult.textContent = result;
          })
          .catch((error) => {
            console.log("error", error);
            alert(error);
          });
    } 
    
    else {
        document.getElementById('submissionResult').textContent = 'Please select either a file or enter a link.';
    }
    // document.getElementById('submissionResult').textContent = 'Submitted';
}


//6. Video preview
function showVideoPreview(url) {
    const videoPreview = document.getElementById('video-preview');
    videoPreview.src = url;
    videoPreview.style.display = 'block';
}

function hideVideoPreview() {
    const videoPreview = document.getElementById('video-preview');
    videoPreview.src = '';
    videoPreview.style.display = 'none';
}

// document.getElementById('close-preview').addEventListener('click', function() {
//     document.getElementById('video-preview').pause(); // Pause the video
//     document.getElementById('video-preview').currentTime = 0; // Reset video to start
//     document.getElementById('video-container').style.display = 'none'; // Hide video container
// });


// //------------------
// // Function to show video preview
// function showVideoPreview(url) {
//     const videoPreview = document.getElementById('video-preview');
//     videoPreview.src = url;
//     videoPreview.style.display = 'block';
// }

// // Function to hide video preview
// function hideVideoPreview() {
//     const videoPreview = document.getElementById('video-preview');
//     videoPreview.src = '';
//     videoPreview.style.display = 'none';
// }

// // Function to handle file input change event
// document.getElementById('fileInput').addEventListener('change', function() {
//     selectedFile = this.files[0];
//     document.getElementById('fileName').textContent = 'Selected File: ' + selectedFile.name;
//     hideLinkInput(); // Hide link input if file is selected
//     showVideoPreview(URL.createObjectURL(selectedFile)); // Show video preview
// });

// // Function to handle link input change event
// document.getElementById('link-input').addEventListener('input', function() {
//     selectedLink = this.value;
//     selectedFile = null;
//     document.getElementById('fileName').textContent = '';
//     hideVideoPreview(); // Hide video preview if link is entered
// });

// // Function to handle form submission
// function submitForm() {
//     if (selectedFile !== null && selectedLink === '') {
//         document.getElementById('submissionResult').textContent = selectedFile.name;
//     } else if (selectedLink !== '' && selectedFile === null) {
//         document.getElementById('submissionResult').textContent = 'Submitted';
//     } else {
//         document.getElementById('submissionResult').textContent = 'Please select either a file or enter a link.';
//     }
// }
