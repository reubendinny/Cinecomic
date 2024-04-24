# Cinecomic
Cinecomic is an automated movie-to-comic generator. Input a video and it generates a comic book for the same complete with a comic style and dialogue bubbles

<img src="https://i.postimg.cc/KcB9QpKq/harry-final.jpg" width=50% height=50%>

## Methodology
Our project consists of the following core modules:
1. **Subtitle Generation**
    - Create a subtitle file for the input video using Whisper model
2. **Keyframe Extraction**
    - Frame Sampling: Samples frames at a set frequency from videos.
    - Feature Extraction: Utilizes deep learning models like GoogLeNet v1 to extract features from frames.
    - Highlightness Score Calculation: Deep Summarization Network (DSN) computes scores to identify keyframes.
    - Dialogue Grouping: Groups frames based on dialogues to select significant keyframes.
3. **Panel Layout Generation**
    - Calculates the Region of Interest of a frame 
    - Selects a page layout template
    - Crops frame to be accomodated into template
4. **Balloon Generation & Placement**
    - Analysis of emotions in subtitles determines speech balloon shape.
    - Balloon placement involves using the "Dlib" face-detector library to detect characters' mouth positions in frames and placing at regions with relatively lesser ROI.
5. **Cartoonization**
    - Applies style transfer algorithms to enhance keyframes visually, mimicking traditional comics.

> Read the project report for detailed explanations

## Pre-requisites
- Python
- All dependencies mentioned in `requirements.txt` to be installed. (`pip install -r requirements.txt`)


## Some more examples
<img src="https://i.postimg.cc/qMr1Fcyk/joker2.jpg" width=50% height=50%>

</br>
<img src="https://i.postimg.cc/qMG1Htx2/narnia.jpg" width=50% height=50%>

