import math
import json
import srt
import pickle
from backend.speech_bubble.lip_detection import get_lips
from backend.speech_bubble.bubble_placement import get_bubble_position
from backend.speech_bubble.bubble_shape import get_bubble_type
from backend.class_def import bubble
import threading

def emotion_detection(subs,emotions):
    # Placeholder for actual emotion detection logic
    with open("test1.srt", "r") as file:
        for sub in subs:
            dialogue = sub.content
            emotions.append(get_bubble_type(dialogue))

    

def bubble_create(video, crop_coords, black_x, black_y):

    bubbles = []
    emotions = []


    # def bubble_create(bubble_cord,lip_cord,page_template):
    data=""
    with open("test1.srt") as f:
        data=f.read()
    subs=srt.parse(data)


    # Start emotion detection in a separate thread
    emotion_thread = threading.Thread(target=emotion_detection, args=(subs, emotions))
    emotion_thread.start()

    # Reading CAM data from dump
    CAM_data = None
    with open('CAM_data.pkl', 'rb') as f:
        CAM_data = pickle.load(f)

    lips = get_lips(video, crop_coords,black_x,black_y)
    # Dumping lips
    with open('lips.pkl', 'wb') as f:
        pickle.dump(lips, f)

    # # Reading lips
    # lips=None
    # with open('lips.pkl', 'rb') as f:
    #     lips = pickle.load(f)
    
    emotion_thread.join()
    print("Detected emotions:", emotions)


    for sub in subs:
        lip_x = lips[sub.index][0]
        lip_y = lips[sub.index][1]

        bubble_x, bubble_y = get_bubble_position(crop_coords[sub.index-1], CAM_data[sub.index-1])

        dialogue = sub.content
        type = get_bubble_type(dialogue)

        temp = bubble(bubble_x, bubble_y,lip_x,lip_y,sub.content)
        bubbles.append(temp)

    return bubbles









