# from backend.subtitles.subs import get_subtitles
# from backend.keyframes.keyframes import generate_keyframes, black_bar_crop
# from backend.panel_layout.layout_gen import generate_layout
# from backend.cartoonize.cartoonize import style_frames
from backend.speech_bubble.lip_detection import get_lips

video = 'video/harry.mp4'
# get_subtitles(video)

# generate_keyframes(video)
# black_bar_crop()

# generate_layout()
# style_frames()
get_lips(video)
