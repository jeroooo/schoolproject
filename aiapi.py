from tkinter import*
from PIL import Image, ImageTk
import requests
from playsound import playsound

def get_duck_image():

    api_url = "https://source.unsplash.com/featured/?duck"

    response = requests.get(api_url)
    
    image = Image.open(requests.get(api_url, stream=True).raw)
    photo = ImageTk.PhotoImage(image)
    
    label.config(image=photo)
    label.image = photo
    b.config(text='STISNI ZA JOŠ JEDNU')
    playsound('1.mp3')

p = Tk()
p.title("Patke patke patkice")

b =Button(p, text="STISNI ZA SLIKU PATKICA", command=get_duck_image)
b.pack()

label = Label(p)
label.pack()

mainloop()
