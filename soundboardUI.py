import PySimpleGUI as GUI
import time
import asyncio
from  audiochanger import audiochanger
from getsoundfiles import getsoundfiles
from pathlib import Path
files=getsoundfiles("sound")
layout=[[GUI.Text("pitch")],[GUI.Radio("low",1,key="low")],[GUI.Radio("None",1, True,metadata=1)],[GUI.Radio("high",1,key="high")]]
mylist=[]
for sound in files:
	name=Path(sound).stem
	mylist.append(name)
	layout.append([GUI.Button(name,key=name)])
soundboard=GUI.Window("BTTV soundboard",layout)

while True:
    event,values=soundboard.read()
    if event in mylist:
        print(values)
        #do shit here
        pitch=1
        soundboard[event].Update(disabled=True)
        if values["low"]==True:
            pitch=-.5
        elif values["high"]==True:
            pitch=.5
        audiochanger.playaudio(event,pitch)
        time.sleep(3)
        soundboard[event].Update(disabled=False)
    #check for closed window
    if event==GUI.WIN_CLOSED:
        break
