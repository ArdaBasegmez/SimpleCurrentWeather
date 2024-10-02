import pytz
import requests
from tkinter import *
from PIL import ImageTk
from datetime import *
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim

Font = ("helvetica", 16)
Font2 = ("consolas", 22, "bold")

API_key = "4433fa83e0579fad10e8e4b921b0bbad"

root = Tk()
root.resizable(width=False, height=False)
root.title("weather screen")
root.minsize(width=570, height=500)
root.config(bg="#d2cde3")

SearchBoard = PhotoImage(file="search_board.png")
search_label = Label(image=SearchBoard, borderwidth=0, bg="#d2cde3")
search_label.place(x=90, y=80)

search_entry = Entry(bg="#181d4e", fg="snow", borderwidth=0, font="Arial 16")
search_entry.place(x=160, y=95)

Label1 = Label(width=38, height=18, bg="#181d4e")
Label1.place(x=10, y=220)

Label2 = Label(width=38, height=18, bg="#181d4e")
Label2.place(x=285, y=220)

tLabel = Label(text="Temperature :", font=Font, bg="#181d4e", fg="snow")
tLabel.place(x=307, y=290)

hLabel = Label(text="Humidity  :", font=Font, bg="#181d4e", fg="snow")
hLabel.place(x=307, y=335)

pLabel = Label(text="Pressure :", font=Font, bg="#181d4e", fg="snow")
pLabel.place(x=307, y=380)

wLabel = Label(text="Wind Speed :", font=Font, bg="#181d4e", fg="snow")
wLabel.place(x=307, y=425)

time = Label(bg="#181d4e", fg="snow", font=Font2)
time.place(x=360, y=260)

Frame1 = Frame(width=547, height=50, bg="#181d4e")
Frame1.place(x=10, y=168)
Day = Label(Frame1, bg="#181d4e", fg="snow", font=Font2)
Day.place(x=10, y=3)
first = datetime.now()
Day.config(text=first.strftime("%A"))

DesFrame = Frame(width=200, height=200, bg="#181d4e", borderwidth=20)
DesFrame.place(x=55, y=270)
image1 = Label(DesFrame, bg="#181d4e")
image1.place(x=20, y=20)
def display_weather():
    city = search_entry.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    json_data = requests.get(api).json()
    temp1 = int(json_data["main"]["temp"]-273.15)
    pressure1 = json_data["main"]["pressure"]
    humidity1 = json_data["main"]["humidity"]
    wind_speed1 = json_data["wind"]["speed"]

    locator = Nominatim(user_agent="geoapiExercises")
    location = locator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    city_time = pytz.timezone(result)
    local_time = datetime.now(city_time)
    current_time = local_time.strftime("%I:%M")
    time.config(text=current_time)

    tLabel.config(text=("Temperature", ":", temp1, "°"))
    hLabel.config(text=("Humidity", ":", "%", humidity1))
    pLabel.config(text=("Pressure", ":", pressure1))
    wLabel.config(text=("Wind", "Speed", ":", wind_speed1, "m/s"))

    description_image = json_data["weather"][0]["icon"]
    photo = ImageTk.PhotoImage(file=f"project/{description_image}.png")
    image1.config(image=photo)
    image1.image = photo

button_image = PhotoImage(file="search_button.png")
search_button = Button(image=button_image, borderwidth=0, command=display_weather)
search_button.config(bg="#d2cde3")
search_button.place(x=440, y=83)

root.mainloop()
