# from backend.subtitles.subs import get_subtitles
from backend.keyframes.keyframes import generate_keyframes, black_bar_crop
from backend.panel_layout.layout_gen import generate_layout
from backend.cartoonize.cartoonize import style_frames
from backend.speech_bubble.bubble import bubble_create
from backend.class_def import Page,panel,bubble
from backend.json_maker import page_create

import json


# video = 'video/harry.mp4'
# # get_subtitles(video)

# generate_keyframes(video)
# black_bar_crop()

page_templates,panels = generate_layout()

bubbles = bubble_create(page_templates)

style_frames()


               


pages = page_create(page_templates,panels,bubbles)

print(page_templates)
print(pages)

pages_dict = []

for page in pages:
    pages_dict.append(page.__dict__)

with open('page.js', 'w') as f:
    f.write(f'var pages = ')
    json.dump(pages_dict, f , indent=4)


