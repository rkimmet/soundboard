from pydub import AudioSegment
from pydub.playback import play
import numpy as np

from playsound import playsound
class audiochanger:

    def pitch_audio(wr,pitch):
        sound=AudioSegment.from_file(wr,format="wav")
        if pitch!=1:
            octaves=pitch
            new_samplerate=int(sound.frame_rate * (1.5**(octaves)))
            hipitch_sound=sound._spawn(sound.raw_data, overrides={'frame_rate': new_samplerate})
            hipitch_sound=hipitch_sound.set_frame_rate(44100)
            sound=hipitch_sound
        play(sound)
    def playaudio(audio,pitch):
        soundname="./sound/"+audio+".wav"
        
        audiochanger.pitch_audio(soundname,pitch)

        
