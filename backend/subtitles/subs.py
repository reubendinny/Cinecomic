import srt
from datetime import timedelta
import stable_whisper
import ffmpeg
import os


def process_srt(file_path, threshold_seconds):
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_content = file.read()
    
    subtitles = list(srt.parse(srt_content))
    threshold = timedelta(seconds=threshold_seconds)
    segment_duration = timedelta(seconds=5)
    new_subtitles = []
    
    def create_action_scene_segments(start_time, total_duration):
        segments = []
        num_segments = total_duration // segment_duration
        remainder = total_duration % segment_duration
        
        current_start = start_time
        for i in range(num_segments):
            segment_end = current_start + segment_duration
            segments.append(srt.Subtitle(
                index=0,  # Will be reindexed later
                start=current_start,
                end=segment_end,
                content='((action-scene))'
            ))
            current_start = segment_end + timedelta(milliseconds=1)
        
        if remainder > timedelta(seconds=3):
            segment_end = current_start + remainder
            segments.append(srt.Subtitle(
                index=0,  # Will be reindexed later
                start=current_start,
                end=segment_end,
                content='((action-scene))'
            ))
        
        return segments
    
    for i in range(len(subtitles) - 1):
        new_subtitles.append(subtitles[i])
        time_diff = subtitles[i + 1].start - subtitles[i].end
        if time_diff > threshold:
            start_time = subtitles[i].end + timedelta(milliseconds=1)
            segments = create_action_scene_segments(start_time, time_diff)
            new_subtitles.extend(segments)
    
    new_subtitles.append(subtitles[-1])
    
    # Reindex subtitles
    new_subtitles = list(srt.sort_and_reindex(new_subtitles))
    
    with open('test1.srt', 'w', encoding='utf-8') as file:
        file.write(srt.compose(new_subtitles))

def extract_audio(file):
    extracted_audio = "audio.mp3"
    stream = ffmpeg.input(file)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

def get_subtitles(file):
    extracted_audio = extract_audio(file)
    model = stable_whisper.load_model('small')
    result = model.transcribe_minimal(extracted_audio)
    result.to_srt_vtt('test1.srt',word_level=False)
    process_srt('test1.srt', 5)
    if os.path.exists(extracted_audio):
        os.remove(extracted_audio)

if __name__ == '__main__':
    get_subtitles('video/joker.mp4')


