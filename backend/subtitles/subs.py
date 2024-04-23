from subsai import SubsAI

def get_subtitles(file):
    subs_ai = SubsAI()
    model = subs_ai.create_model('openai/whisper', {'model_type': 'medium'})
    subs = subs_ai.transcribe(file, model)
    subs.save('test1.srt')