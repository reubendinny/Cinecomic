import pickle
# from backend.subtitles.subs import get_subtitles
# from backend.keyframes.keyframes import generate_keyframes, black_bar_crop
# from backend.panel_layout.layout_gen import generate_layout
# from backend.cartoonize.cartoonize import style_frames
from backend.speech_bubble.lip_detection import get_lips

video = 'video/harry.mp4'
# get_subtitles(video)

# generate_keyframes(video)
# black_x, black_y, _, _ = black_bar_crop()

# crop_coords = generate_layout()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # Dumping crop_coords and black_coords
# with open('crop_coords.pkl', 'wb') as f:
#     pickle.dump(crop_coords, f)
# with open('black_coords.pkl', 'wb') as f:
#     pickle.dump((black_x,black_y), f)

# ==============================================
# Reading crop_coords and black_coords
crop_coords=None
black_coords=None
with open('crop_coords.pkl', 'rb') as f:
    crop_coords = pickle.load(f)
with open('black_coords.pkl', 'rb') as f:
    black_coords = pickle.load(f)
black_x = black_coords[0]
black_y = black_coords[1]
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# style_frames()
get_lips(video, crop_coords,black_x,black_y)
