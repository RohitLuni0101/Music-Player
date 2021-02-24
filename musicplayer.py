from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter import messagebox
from tkinter.ttk import Progressbar


class Main:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("700x500+0+0")

        # change the title of the window
        self.win.title("Music Player")

        # Global variable
        self.audiotrak = StringVar()
        self.text3 = StringVar()
        self.currentvol = 0

        # Creating Menubar
        self.menubar = Menu(self.win)

        mixer.init()

        # Adding File Menu and commands
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Media', menu=self.file)
        self.file.add_command(label='Open File', command=self.openfile)
        self.file.add_command(label='Open Folder', command=self.openfile)
        self.file.add_command(label='Play', command=self.playmusic)
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.win.destroy)

        # Adding Edit Menu and commands
        self.edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=self.edit)
        self.edit.add_command(label='pause', command=self.pausemusic)
        self.edit.add_command(label='resume', command=self.resumemusic)
        self.edit.add_command(label='Stop', command=self.stopmusic)
        self.edit.add_command(label='Increase Volume', command=self.volumeup)
        self.edit.add_separator()
        self.edit.add_command(label='Decrease Volume', command=self.volumedown)
        self.edit.add_command(label='Find again', command=None)

        # Adding Help Menu
        self.help_ = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.help_)
        self.help_.add_separator()
        self.help_.add_command(label='About Me', command=None)

        self.progresbar = Progressbar(self.win, orient=VERTICAL, mode='determinate', value=0, length=100).place(x=650, y=375)

        self.txt=Label(self.win, width=60,textvariable=self.audiotrak, font="arial 15",).place(x=10, y=5)
        self.txt2=Label(self.win, width=34,text='Simple Music Player Develop By Rohit Luni',fg='red', font="arial 30",).place(x=0, y=190)
        self.txt3=Label(self.win, width=10,textvariable=self.text3,fg='red', font="arial 20",).place(x=260, y=250)

        self.pausebutton = Button(self.win, text="Pause", bg='dark green', fg='white', command=self.pausemusic)
        self.pausebutton.grid(row=0,column=0, padx=100, pady=450)

        self.resumebutton = Button(self.win, text="Resume", bg='dark green', fg='white', command=self.resumemusic)
        self.resumebutton.grid(row=0,column=0, padx=100, pady=450)
        self.resumebutton.grid_remove()

        self.playbutton = Button(self.win, text="Play", bg='dark green', fg='white', command=self.playmusic)
        self.playbutton.place(x=180, y=450)

        self.stopbutton = Button(self.win, text="Stop", bg='red', fg='white', command=self.stopmusic)
        self.stopbutton.place(x=250, y=450)

        self.volumeupbutton = Button(self.win, text="Volume +", bg='dark green', fg='white', command=self.volumeup)
        self.volumeupbutton.place(x=330, y=450)

        self.volumedownbutton = Button(self.win, text="Volume -", bg='dark green', fg='white', command=self.volumedown)
        self.volumedownbutton.place(x=520, y=450)

        self.mutebutton = Button(self.win, text="Mute", bg='dark green', fg='white', command=self.mute)
        self.mutebutton.grid(row=0,column=1, padx=190, pady=450)

        self.unmutebutton = Button(self.win, text="Unmute", bg='dark green', fg='white', command=self.unmute)
        self.unmutebutton.grid(row=0,column=1, padx=190, pady=450)
        self.unmutebutton.grid_remove()

        self.win.config(menu=self.menubar)
        self.win.mainloop()

    def openfile(self):
        try:
            self.ms = filedialog.askopenfilename(filetype=(('MP3', '*.mp3'), ('WAV', '*.wav')), titel='Select Audio File')

        except:
            self.ms = filedialog.askopenfilename()

        self.audiotrak.set(self.ms)

    def playmusic(self):
        self.ad =self.audiotrak.get()
        print(self.ad)
        mixer.music.load(self.ad)
        mixer.music.play()
        self.text3.set('Playing......')

    def pausemusic(self):
        mixer.music.pause()
        self.pausebutton.grid_remove()
        self.resumebutton.grid()
        self.text3.set('Pause')


    def resumemusic(self):
        self.pausebutton.grid()
        self.resumebutton.grid_remove()
        mixer.music.unpause()
        self.text3.set('Playing......')


    def stopmusic(self):
        mixer.music.stop()
        self.text3.set('Stop')

    def volumeup(self):
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol+0.05)
        self.progresbar['value'] = 100


    def volumedown(self):
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol-0.05)

        self.progresbar['value'] = 100


    def mute(self):
        self.mutebutton.grid_remove()
        self.unmutebutton.grid()
        self.currentvol = mixer.music.get_volume()
        mixer.music.set_volume(0)
        self.text3.set('Mute')

    def unmute(self):
        self.unmutebutton.grid_remove()
        self.mutebutton.grid()
        mixer.music.set_volume(self.currentvol)
        self.text3.set('Playing......')


if __name__ == "__main__":
    x = Main()
