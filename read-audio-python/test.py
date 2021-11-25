import soundfile as sf
import deepspeech
import numpy as np
import os
import wave
import librosa
from mcipc.rcon.je import Client
import re

#og audio
directory = './rawaudio'
#fucky wav audio
wav_directory = './bruhaudio'
#jesus christ
audio_direc = './audio'

model_file_path = 'deepspeech-0.9.3-models.pbmm'
model = deepspeech.Model(model_file_path)

scorer_file_path = 'deepspeech-0.9.3-models.scorer'
model.enableExternalScorer(scorer_file_path)
lm_alpha = 0.90
lm_beta = 2.10
model.setScorerAlphaBeta(lm_alpha, lm_beta)

count = 0

beam_width = 1265
model.setBeamWidth(beam_width)

for filename in os.listdir(directory):
    os.remove('./rawaudio/%s' % filename)
for filename in os.listdir(wav_directory):
    os.remove('./bruhaudio/%s' % filename)
for filename in os.listdir(audio_direc):
    os.remove('./audio/%s' % filename)

while(True):
    for filename in os.listdir(directory):
        #print("converting %s to .wav" % filename)
        data, fs = sf.read('./rawaudio/%s' % filename,
                          channels=2, samplerate=48000, format='RAW', subtype='PCM_16')
        sf.write('./bruhaudio/%s.wav' % filename, data, fs)
        os.remove('./rawaudio/%s' % filename)

    for filename in os.listdir(wav_directory):
        #print("converting %s to 16000" % filename)
        try:
            y, s = librosa.load('./bruhaudio/%s' % filename, sr=16000)
        except ValueError:
            continue
        sf.write('./audio/%s' % filename, y, s)
        os.remove('./bruhaudio/%s' % filename)
    
    for filename in os.listdir(audio_direc):
        #print("looking at %s" % filename)
        w = wave.open('./audio/%s' % filename)
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)

        temp = filename.split("#")
        
        data16 = np.frombuffer(buffer, dtype=np.int16)

        text = model.stt(data16)

        if not text == "":
            print(str(temp[0]) + ": " + text)

        if re.search("e|E", text):
            count += 1
            with Client('localhost', 25575, passwd="password") as client:
                client.say("§lOffense §l#%s" % count)
                client.say(temp[0] + " said: " + text)
                client.kill("@a")
                
        w.close()
        os.remove('./audio/%s' % filename)