import math
import json
import srt
from backend.class_def import bubble




def bubble_create(page_template):

    bubbles = []

    # def bubble_create(bubble_cord,lip_cord,page_template):
    data=""
    with open("test1.srt") as f:
        data=f.read()

    subs=srt.parse(data)



    for sub in subs:
        temp = bubble(4,1,2,2,sub.content)
        bubbles.append(temp)

    return bubbles
    # with open('bubble.js', 'a') as f:
    #     json.dump(bubbles, f , indent=4)
    # f.close()









