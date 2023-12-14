#py -m pip install pillow u commnad promptu
#py -m pip install pygame u commnad promptu
from tkinter import*
from PIL import Image, ImageTk
import requests
from playsound import playsound
from pygame import mixer







#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('1.mp3')

print("music started playing....")

#Set preferred volume
mixer.music.set_volume(0.2)

#Play the music
mixer.music.play()

def get_duck_image():

    api_url = "https://source.unsplash.com/featured/?duck"

    response = requests.get(api_url)
    
    image = Image.open(requests.get(api_url, stream=True).raw)
    photo = ImageTk.PhotoImage(image)
    
    label.config(image=photo)
    label.image = photo
    b.config(text='STISNI ZA JOŠ JEDNU')
    mixer.music.play()

p = Tk()
p.title("Patke patke patkice")

b =Button(p, text="STISNI ZA SLIKU PATKICA", command=get_duck_image)
b.pack()

label = Label(p)
label.pack()

mainloop()
