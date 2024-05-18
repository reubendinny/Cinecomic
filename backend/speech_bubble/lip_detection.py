import dlib
import cv2
import os
import srt
import re
from math import floor,sqrt
from backend.utils import convert_to_css_pixel

# Some constants
THETA1 = 1.2    # Difference between lip distance of prev and curr frame
THETA2 = 0.4    # No. of lips crossed ratio
SAMPLE_RATE = 5 
FACE_AREA = 0.6 

# Face detector and landmark detector
face_detector = dlib.get_frontal_face_detector()   
landmark_detector = dlib.shape_predictor("backend/speech_bubble/shape_predictor_68_face_landmarks.dat")


def dist(p1, p2):
    p1_x = p1[0]
    p2_x = p2[0]
    p1_y = p1[1]
    p2_y = p2[1]
    dist = sqrt((p2_x - p1_x) ** 2 + (p2_y - p1_y) ** 2)
    return dist

# Checks if 2 face rectangles have the same area using their top-left and bottom-right corners
def similar_to_keyframe(face_rects, keyframe_face_rects):
    rect1_top_left = face_rects[0].tl_corner()
    rect1_bottom_right = face_rects[0].br_corner()
    rect2_top_left = keyframe_face_rects[0].tl_corner()
    rect2_bottom_right = keyframe_face_rects[0].br_corner()
    tolerance = 0.2
    
    def calculate_area(top_left, bottom_right):
        width = abs(bottom_right.x - top_left.x)
        height = abs(bottom_right.y - top_left.y)
        return width * height

    area_rect1 = calculate_area(rect1_top_left, rect1_bottom_right)
    area_rect2 = calculate_area(rect2_top_left, rect2_bottom_right)
    
    area_tolerance = area_rect1 * tolerance
    
    if abs(area_rect1 - area_rect2) <= area_tolerance:
        return True
    else:
        return False

#crop_coords contain left,right,top,bottom of each frame
def get_lips(video, crop_coords, black_x, black_y):
    print(crop_coords)
    data=""
    with open("test1.srt") as f:
        data = f.read()
    subs = srt.parse(data)

    lips = {}
    for sub in subs:  
        keyframe_path = f"frames/final/frame{sub.index:03}.png"
        keyframe = cv2.imread(keyframe_path)
        gray = cv2.cvtColor(keyframe,cv2.COLOR_BGR2GRAY)   # Convert image into grayscale
        face_rects = face_detector(gray,1)             # Detect face
        print("\nsub:",sub.index)
        if sub.content == "((action-scene))":
            print("skipping action scene")
            lips[sub.index] = (-1,-1)
            continue

        if len(face_rects) < 1:                 # No face detected
            print("No face detected: ",sub)
            lips[sub.index] = (-1,-1)
            continue

        if len(face_rects) == 1:                # 1 face detected: Extract from keyframe itself
            rect = face_rects[0]
            landmark = landmark_detector(gray, rect)   # Detect face landmarks
            x,y = convert_to_css_pixel(landmark.part(65).x, landmark.part(65).y, crop_coords[sub.index - 1])
            lips[sub.index] = (x,y)
            continue

            
        if len(face_rects) > 1:                  # Too many face detected
            print("Too many face: sub_",sub.index,": ", len(face_rects))
            origin = (crop_coords[sub.index - 1][0] , crop_coords[sub.index - 1][2] ) # (left,top)
            lip_coords = get_multi_speaker_lips(sub,video,face_rects)
            if lip_coords == (-1,-1):
                lips[sub.index] = (-1,-1)
            else:
                x = lip_coords[0] - (origin[0] + black_x)
                y = lip_coords[1] - (origin[1] + black_y)
                x , y = convert_to_css_pixel(x,y,crop_coords[sub.index - 1])
                lips[sub.index] = (x,y)
            continue
    print(lips)
    return lips


def get_multi_speaker_lips(sub,video, keyframe_face_rects):
    start_time = sub.start.total_seconds()
    end_time = sub.end.total_seconds()
    keyframe_path = f"frames/final/frame{sub.index:03}.png"

    vid = cv2.VideoCapture(video)       # Read video
    frames_per_sec = vid.get(cv2.CAP_PROP_FPS)  # Number of frames per second
    # total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) 
    # frames_count = total_frames // frameRate  

    # Calculate the frame skip value
    select_index = floor(frames_per_sec / SAMPLE_RATE)  # Select every (skip_rate)'th position frames to get the SAMPLE_RATE number of frames per second
    start_frame = int(start_time * frames_per_sec)
    end_frame = int(end_time * frames_per_sec)

    vid.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    print("FPS,  select index = ", frames_per_sec, select_index)

    # Initialize frame counter
    current_frame = start_frame
    total_frames_selected = 0

    # Parse into frames 
    frame_buffer = []               # A list to hold frame images
    frame_buffer_color = []         # A list to hold original frame images
    while(current_frame<end_frame):
        success, frame = vid.read()                # Read frame
        if not success:
            break 
        if current_frame % select_index == 0:                          # Break if no frame to read left
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # Convert image into grayscale
            frame_buffer.append(gray)                  # Add image to the frame buffer
            frame_buffer_color.append(frame)
            total_frames_selected += 1
        current_frame += 1
    vid.release()

    prev_lip_dist = {}      #2D[i][j]
    lip_motion_count = {}   #1D[j]
    lip_coords = {}         #1D[j]
    avg_gap = {}            #2D[i][j]

    start_flag = False      #To skip the lip distance calculation for first frame

    for (i, image) in enumerate(frame_buffer):          # Iterate on frame buffer
        face_rects = face_detector(image,1)             # Detect face
        if len(face_rects) < 1:                 # No face detected
            print("No face detected: frame ",i)
            continue
        if len(face_rects) >= 1:                  # Too many face detected

            # Check if area of the first face rectangle is close to keyframe
            if not similar_to_keyframe(face_rects, keyframe_face_rects):
                print("frame not similar: ",i)
                continue

            largest_face = max(face_rects, key=lambda rect: rect.area())
            print("largest face: ", largest_face)

            avg_gap[i] = {}
            prev_lip_dist[i] = {}
            for (j,rect) in enumerate(face_rects):
                if (rect.area() / largest_face.area()) < FACE_AREA:     #Consider lip only if face area crosses a threshold(ROI)
                    print("Lip skipped: ", j, rect)
                    continue

                prev_lip_dist[i][j] = 0
                landmark = landmark_detector(image, rect)   # Detect face landmarks
                # landmark = shape_to_list(landmark)

                part_61 = (landmark.part(61).x,landmark.part(61).y)
                part_67 = (landmark.part(67).x,landmark.part(67).y)
                part_62 = (landmark.part(62).x,landmark.part(62).y)
                part_66 = (landmark.part(66).x,landmark.part(66).y)
                part_63 = (landmark.part(63).x,landmark.part(63).y)
                part_65 = (landmark.part(65).x,landmark.part(65).y)
                A = dist(part_61, part_67)
                B = dist(part_62, part_66)
                C = dist(part_63, part_65)

                avg_gap[i][j] = (A + B + C) / 3.0

                # Store lip coordinate if encountered for first time
                if j not in lip_coords:
                    lip_coords[j] = part_65

                # Loop runs for the first time
                if start_flag==False:
                    prev_lip_dist[i][j] = avg_gap[i][j]
                    start_flag = True
                    continue
                
                # Check if lip distance between continous frame is above threshold, if so increase lip count
                print("Difference for frame {0}, lip {1}: {2}".format( i, j, abs(avg_gap[i][j] - prev_lip_dist[i][j])) )
                if abs(avg_gap[i][j] - prev_lip_dist[i][j]) > THETA1:
                    lip_motion_count[j] = lip_motion_count.get(j,0) + 1
                prev_lip_dist[i][j] = avg_gap[i][j]

   
    print("Lip motion count, total_frames_selected = ", lip_motion_count, total_frames_selected)
    # print("max lip count ratio = ", lip_motion_count / (total_frames_selected-1))
    try:
        max_lip_index = max(lip_motion_count, key=lip_motion_count.get)
        # max_value = lip_motion_count[max_lip_index]
        # if max_lip_count / (total_frames_selected-1) > THETA2:
        #     print("speaking")
        if lip_motion_count[max_lip_index] / (total_frames_selected-1) > THETA2:
            return lip_coords[max_lip_index]
        else:
            return (-1,-1)
    except ValueError:
        return (-1,-1)
    except ZeroDivisionError:
        return (-1,-1)

    

    
