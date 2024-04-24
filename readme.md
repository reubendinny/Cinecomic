# Cinecomic
Cinecomic is an automated movie-to-comic generator. Input a video and it generates a comic book for the same complete with a comic style and dialogue bubbles

<img src="https://private-user-images.githubusercontent.com/30729856/325309475-9dfdbd0e-c318-4cb2-9181-59dbf1337736.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM5Nzc0MzAsIm5iZiI6MTcxMzk3NzEzMCwicGF0aCI6Ii8zMDcyOTg1Ni8zMjUzMDk0NzUtOWRmZGJkMGUtYzMxOC00Y2IyLTkxODEtNTlkYmYxMzM3NzM2LmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQyNFQxNjQ1MzBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05MWZkZjE4MjVlMjViMzNiN2VlNGEzMDQ4NmVmOTQ4NmJiZmRiYWU2OWYxOTY5Y2RlMjEyMDkyOGNkMmI0OWY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.slFIXWCJF7Q0-R9Zn2OFqEH-Ddxpxcqsq6xjxxN8hls" width=50% height=50%>

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
<img src="https://private-user-images.githubusercontent.com/30729856/325327623-171ece41-a422-4324-8033-04a429b02b29.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM5ODA4ODIsIm5iZiI6MTcxMzk4MDU4MiwicGF0aCI6Ii8zMDcyOTg1Ni8zMjUzMjc2MjMtMTcxZWNlNDEtYTQyMi00MzI0LTgwMzMtMDRhNDI5YjAyYjI5LmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQyNFQxNzQzMDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZjc3MjMwNWRjNzZhZTc3ZWViZjIzNjFkZjJmM2Y2MjE1YjgzMGIwMTY1ZDdlYWMyMjQ5MDhhZmExNmNmNzgyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.-eKL0Av8pKrf55awo110v_jjW-aA4Abl_rXGDoaCTp8" width=50% height=50%>

</br>
<img src="https://private-user-images.githubusercontent.com/30729856/325328118-52fd4e7c-da78-40c3-b940-d0d3baed1b06.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTM5ODA5ODksIm5iZiI6MTcxMzk4MDY4OSwicGF0aCI6Ii8zMDcyOTg1Ni8zMjUzMjgxMTgtNTJmZDRlN2MtZGE3OC00MGMzLWI5NDAtZDBkM2JhZWQxYjA2LmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNDI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDQyNFQxNzQ0NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZWY0MjIwOTcyYWNkZTdkZDU3NTE5Nzk4OTliMGE2NDY2Nzk3MmZiMjBhYTI5YzY1OGY1YzBmMTZjYjBiODMyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.9rpRqWe8lJa5hYBLi0vzmUM3nbxIFcVP_K2W7XPF_uI" width=50% height=50%>

