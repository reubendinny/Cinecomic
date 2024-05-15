import os
import shutil
from pytube import YouTube 

from flask import Flask, render_template,request
from backend.subtitles.subs import get_subtitles
from backend.keyframes.keyframes import generate_keyframes, black_bar_crop
from backend.panel_layout.layout_gen import generate_layout
from backend.cartoonize.cartoonize import style_frames
from backend.speech_bubble.bubble import bubble_create
from backend.page_create import page_create,page_json
from backend.utils import cleanup, download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index4.html')


def create_comic():
    video = 'video/uploaded.mp4'
    get_subtitles(video)
    generate_keyframes(video)
    black_x, black_y, _, _ = black_bar_crop()
    crop_coords, page_templates, panels = generate_layout()
    bubbles = bubble_create(video, crop_coords, black_x, black_y)
    pages  = page_create(page_templates,panels,bubbles)
    page_json(pages)
    style_frames()

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(dict(request.form))  
        f = request.files['file']  #we got the file as file storage object from frontend
        print(type(f))
        f.save("video/uploaded.mp4")
        cleanup()
        create_comic()
        return "Comic created Successfully"
    
@app.route('/handle_link', methods=['GET', 'POST'])
def handle_link():
    if request.method == 'POST':
        print(dict(request.form))  
        link = request.form['link']
        download_video(link)
        cleanup()
        create_comic()
        return "Comic created Successfully"
    
