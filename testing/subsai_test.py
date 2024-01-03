from subsai import SubsAI

file = './video/harry.mp4'
subs_ai = SubsAI()
model = subs_ai.create_model('openai/whisper', {'model_type': 'base'})
subs = subs_ai.transcribe(file, model)
subs.save('test1.srt')

