import pickle
from backend.subtitles.subs import get_subtitles
from backend.keyframes.keyframes import generate_keyframes, black_bar_crop
from backend.panel_layout.layout_gen import generate_layout
from backend.cartoonize.cartoonize import style_frames
from backend.speech_bubble.bubble import bubble_create
from backend.page_create import page_create,page_json
from backend.utils import cleanup

cleanup()
video = 'video/uploaded.mp4'
get_subtitles(video)

generate_keyframes(video)
black_x, black_y, _, _ = black_bar_crop()

crop_coords, page_templates, panels = generate_layout()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Dumping crop_coords and black_coords
# with open('crop_coords.pkl', 'wb') as f:
#     pickle.dump(crop_coords, f)
# with open('black_coords.pkl', 'wb') as f:
#     pickle.dump((black_x,black_y), f)
# with open('page_templates.pkl', 'wb') as f:
#     pickle.dump(page_templates, f)
# with open('panels.pkl', 'wb') as f:
#     pickle.dump(panels, f)
# ==============================================
# Reading crop_coords and black_coords
# crop_coords=None
# black_coords=None
# page_templates=None
# with open('crop_coords.pkl', 'rb') as f:
#     crop_coords = pickle.load(f)
# with open('black_coords.pkl', 'rb') as f:
#     black_coords = pickle.load(f)
# with open('page_templates.pkl', 'rb') as f:
#     page_templates = pickle.load(f)
# with open('panels.pkl', 'rb') as f:
#     panels = pickle.load(f)
# black_x = black_coords[0]
# black_y = black_coords[1]
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    
bubbles = bubble_create(video, crop_coords, black_x, black_y)

pages  = page_create(page_templates,panels,bubbles)

page_json(pages)

style_frames()
