from tkinter import *
import requests


def show_response(weather):
    try:
        cityName = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        city["text"] = cityName
        temperature["text"] = str(int(temp)) + "°C"
        description["text"] = desc
    except Exception:
        city["text"] = "Intente nuevamente"



def weather_JSON(city):
    try:
        API_key = "YOURAPIKEY"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parameters = {"APPID" : API_key, "q": city, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parameters)
        weather = response.json()
        show_response(weather)
    except Exception:
        print("Error")
        

window = Tk()
window.geometry("500x500")  
window.title("WEATHER APP")

city_text = Entry(window, font = ("Courier", 20, "normal"), justify = "center")  
city_text.pack(padx = 30, pady = 30,)  

get_weather = Button(window, text = "Obtener Clima", font = ("Courier", 20, "normal"), command = lambda: weather_JSON(city_text.get()))
get_weather.pack(pady = 20)

city = Label(font = ("Courier", 20, "normal"), justify = "center")
city.pack(padx = 20, pady = 30)

temperature = Label(font = ("Courier", 50, "normal"), justify = "center")
temperature.pack(padx = 10, pady = 10)

description = Label(font = ("Courier", 20, "normal"), justify = "center")
description.pack(padx = 10, pady = 10)


window.mainloop()