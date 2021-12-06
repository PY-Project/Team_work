import os
import pickle
import tkinter as tk
from tkinter import LabelFrame, PhotoImage
from tkinter import filedialog
from abc import ABCMeta,abstractmethod

class AbstractBaseClass(tk.Frame,metaclass=ABCMeta):

    def __create_frame(self):
        pass

    def __create_widget(self):
        pass

class Track(AbstractBaseClass):

    def __create_frame(self):

        self.track = tk.LabelFrame(self,text = 'Sound Track',
            font = ('times 15 bold italic'),bg = 'black',fg ='white',bd=5,relief=tk.GROOVE)

        self.track.configure(width=410,height=300)

        self.track.grid(row=0,column=0,padx=10,pady=5)

    def __create_widget(self):

        self.canvas = tk.Label(self.track,image = img)

        self.canvas.configure(width=395,height=240)

        self.canvas.grid(row=0,column=0)

        self.label = tk.Label(self.track,font=('times 15 bold italic'),
            bg = 'white',fg ='black')

        self.label['text'] = 'Sound MP3 Player'

        self.label.configure(width=30,height=1)

        self.label.grid(row=1,column=0)

class TrackList(AbstractBaseClass):

    playlist = []

    def __create_frame(self):

        self.track_list = tk.LabelFrame(self,text = f'Play_list - {len(TrackList.playlist)}',
            font = ('times 15 bold italic'),bg = 'grey',fg ='white',bd=5,relief=tk.GROOVE)

        self.track_list.configure(width=190,height=391)

        self.track_list.grid(row=0,column=1,rowspan=3,pady=5)

    def __create_widget(self):
        pass

class Controls(AbstractBaseClass):

    def __create_frame(self):

        self.controls = tk.LabelFrame(self,font = ('times 15 bold italic'),
            bg = 'white',relief=tk.GROOVE)

        self.controls.configure(width=410,height=80)

        self.controls.grid(row=2,column=0,padx=5,pady=5)

    def __create_widget(self):

        self.load_songs = tk.Button(self.controls,
            bg ='black', fg='white',font = ('times 15 bold italic'))
        self.load_songs['text'] = 'Load Sounds'
        self.load_songs.grid(row=0,column=0,padx=10,pady=5)

        self.pre = tk.Button(self.controls,image = pre)
        self.pre.grid(row=0,column=1)

        self.pause = tk.Button(self.controls,image = pause)
        self.pause.grid(row=0,column=2)

        self.next = tk.Button(self.controls,image = next)
        self.next.grid(row=0,column=3)

        self.volume = tk.DoubleVar()
        self.slider = tk.Scale(self.controls,from_=0,to=100,orient=tk.HORIZONTAL,bg='white')
        self.slider['variable'] = self.volume
        self.slider.set(55)
        self.slider.grid(row=0,column=4,padx=10)

class Player(Track,TrackList,Controls): 

    def __init__(self,master):

        super().__init__(master)

        self.master = master

        self._Track__create_frame()

        self._TrackList__create_frame()

        self._Controls__create_frame()

        self._Track__create_widget()

        self._TrackList__create_widget()

        self._Controls__create_widget()

        self.pack()



root = tk.Tk()
root.geometry('655x400')
root.wm_title('Sound Player')

img = PhotoImage(file=r'D:\College\Python_project\Music_Player\images\music(3).png')
next = PhotoImage(file=r'D:\College\Python_project\Music_Player\images\next.png')
pre = PhotoImage(file=r'D:\College\Python_project\Music_Player\images\prev.png')
play = PhotoImage(file=r'D:\College\Python_project\Music_Player\images\play.png')
pause = PhotoImage(file=r'D:\College\Python_project\Music_Player\images\pause.png')

obj = Player(master = root)
obj.mainloop()

