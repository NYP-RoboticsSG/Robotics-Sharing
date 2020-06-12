# need to install vlc player first
from tkinter import *
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc

def sel():
    # selection = "You selected the option " + str(var.get())
    # label.config(text = selection)
    # print(var.get())
    if var.get() == 1 :
        url="https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac"
        station = 933
    elif var.get() == 2:
        url="http://playerservices.streamtheworld.com/api/livestream-redirect/883JIA.mp3"
        station = 933
    elif var.get() == 3:
        url="https://playerservices.streamtheworld.com/api/livestream-redirect/CAPITAL958FMAAC.aac"
        station = 958
    elif var.get() == 4:
        url="http://playerservices.streamtheworld.com/api/livestream-redirect/MONEY_893.mp3"
        station = 893
    elif var.get() ==5:
        url="https://playerservices.streamtheworld.com/api/livestream-redirect/CLASS95AAC.aac"
        station = 95
    elif var.get() == 6:
        url="https://playerservices.streamtheworld.com/api/livestream-redirect/938NOWAAC.aac"
        station = 938
    elif var.get() == 7:
        url="data\\11 Reality.mp3"
        station = "Reality"
    elif var.get() == 8:
        url="..\\..\\Videos\\Pokemon_the_Movie_XY.mp4"
        station = "Pokemon the Movie XY"
    elif var.get()== 9:
        url="https://ic1.sslstream.com/kflr-fm?rnd=4573"
        #url = "https://playerservices.streamtheworld.com/api/livestream-redirect/GOLD905AAC.aac"
        station = "Family Life Radio"
        # station = "GOLD90.5"
    elif var.get() == 10:
        url="https://playerservices.streamtheworld.com/api/livestream-redirect/987FMAAC.aac"
        station = "987Hit Maker"
        #https://www.christiannetcast.com/listen/player.asp?station=kflr-fm
    selection = "You selected the option " + str(station)
    label.config(text = selection)
    #Define VLC media
    media=instance.media_new(url)
    #Set player media
    player.set_media(media)
    player.play()

def callback():
    player.stop()

root = Tk()
root.title("Internet Radio Station")
var = IntVar()
w = Label(root, text="Internet Radio Station !", font='Arial 18',padx = 20,pady = 20)
w.pack()

R1 = Radiobutton(root, text="933", font='Arial 18',variable=var, value=1,
                  command=sel)
R1.pack( anchor = W, padx = 5, pady = 5  )

R2 = Radiobutton(root, text="883", font='Arial 18', variable=var, value=2,
                  command=sel)
R2.pack( anchor = W, padx = 5, pady = 5  )

R3 = Radiobutton(root, text="958", font='Arial 18', variable=var, value=3,
                  command=sel)
R3.pack( anchor = W, padx = 5, pady = 5 )

R4 = Radiobutton(root, text="89.3", font='Arial 18', variable=var, value=4,
                  command=sel)
R4.pack( anchor = W , padx = 5, pady = 5 )

R4 = Radiobutton(root, text="95", font='Arial 18', variable=var, value=5,
                  command=sel)
R4.pack( anchor = W, padx = 5, pady = 5  )

R5 = Radiobutton(root, text="938", font='Arial 18', variable=var, value=6,
                  command=sel)
R5.pack( anchor = W, padx = 5, pady = 5 )

R6 = Radiobutton(root, text="Reality", font='Arial 18', variable=var, value=7,
                  command=sel)
R6.pack( anchor = W, padx = 5, pady = 5 )

R7 = Radiobutton(root, text="Pokemon the Movie XY", font='Arial 18', variable=var, value=8,
                  command=sel)
R7.pack( anchor = W, padx = 5, pady = 5 )

R8 = Radiobutton(root, text="Family Life Radio", font='Arial 18', variable=var, value=9,
                   command=sel)
# R8 = Radiobutton(root, text="GOLD90.5", font='Arial 18', variable=var, value=9,
#                   command=sel)
R8.pack( anchor = W, padx = 5, pady = 5 )

R9 = Radiobutton(root, text="98.7 HIt Maker", font='Arial 18', variable=var, value=10,
                  command=sel)
R9.pack( anchor = W, padx = 5, pady = 5 )

b = Button(root, text="STOP", command=callback)
b.pack()
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
#Define VLC player
player=instance.media_player_new()

label = Label(root,height=1,width=40)

label.pack()
root.mainloop()
