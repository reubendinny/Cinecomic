import srt,os
from extract_frames import extract_frames

data=""
with open("test1.srt") as f:
    data = f.read()
    
subs = srt.parse(data)
for sub in subs:
    if not os.path.exists(f"frames/sub{sub.index}"):
        os.makedirs(f"frames/sub{sub.index}")
    extract_frames("video/motivation.mp4",f"frames/sub{sub.index}",sub.start.total_seconds(),sub.end.total_seconds(),2)
    # print(sub)