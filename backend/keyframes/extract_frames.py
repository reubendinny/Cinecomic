import cv2
import os

def extract_frames(input_video, output_path, start_time, end_time, frame_rate):
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    current_frame = start_frame

    frame_count=0
    frames = []
    while current_frame < end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        if current_frame % int(fps / frame_rate) == 0:
            # Save the frame
            frame_name = f"{output_path}/frame_{frame_count}.png"  # You can change the format to PNG, etc.
            frame_filename = f"frame_{frame_count}.png"
            frame_path = os.path.join(output_path, frame_filename)
            frames.append(frame_path)
            cv2.imwrite(frame_name, frame)
            frame_count+=1

        current_frame += 1

    # In case no frames were extracted, we take the first frame
    if not frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        ret, frame = cap.read()
        frame_name = f"{output_path}/frame_0.png"  # You can change the format to PNG, etc.
        frame_filename = f"frame_0.png"
        frame_path = os.path.join(output_path, frame_filename)
        frames.append(frame_path)
        cv2.imwrite(frame_name, frame)

    cap.release()
    return frames