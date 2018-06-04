from gtts import gTTS

# Change the number list every time you run the program to get new pronounciation.
number_list = ['śūnya','ek','duī','tin','chār','pāṅch','chha','sāṭ','āth','nau']
def convert_to_sound(text_to_save):
    tts = gTTS(text=text_to_save, lang='hi')
    tts.save('audio/'+text_to_save+'.mp3')

for a in number_list:
    convert_to_sound(a)