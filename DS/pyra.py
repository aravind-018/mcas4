from gtts import gTTS

text="Hello Sweety! How are You?"

tts=gTTS(text=text, lang="en")

tts.save("voice.mp3")

print("voice saved successfully")