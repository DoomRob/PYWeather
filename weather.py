from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import ttkbootstrap as ttk

# Root
root = ttk.Window(themename="vapor")
root.title("What is the Weather Today?")
root.iconbitmap('c:/Users/corru/OneDrive/Documents/Python/GUI/weather')
root.geometry("800x400")

# https://home.openweathermap.org/

# Collects Weather Data from the API Key
def getWeather(city):
    weatherAPI_Key = "0e115998326124940824a580331df80d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weatherAPI_Key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error, City could not be found")
        return None
    
    # To receive the weather information
    weather = res.json()
    idIcon = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Collects the icon URL and displays the images
    url_icon =f"https://openweathermap.org/img/wn/{idIcon}@2x.png"
    return(url_icon, temperature, description, city, country)

def search():
    city = entryCity.get()
    result = getWeather(city)
    if result is None:
        return
    # Display weather information if city is found
    url_icon, temperature, description, city, country = result
    locationLabel.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(url_icon, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    iconLabel.configure(image=icon)
    iconLabel.image = icon

    tempLabel.configure(text=f"Temperature: {temperature:.2f}°C")
    descriptionLabel.configure(text=f"Description: {description}")

# Enter City Name - Entry Widgets
entryCity = ttk.Entry(root, font=("Arial", 16))
entryCity.pack(pady=10)

# Search for the information of the current weather
searchButton = ttk.Button(root, text="Search", command=search, bootstyle="warning")
searchButton.pack(pady=10)

# Shows City/Country Name
locationLabel = Label(root, font=("Arial", 16))
locationLabel.pack(pady=20)

# Shows Weather Icon
iconLabel = Label(root)
iconLabel.pack()

# Shows the temperature
tempLabel = ttk.Label(root, font=("Arial", 16))
tempLabel.pack()

# Shows Weather description
descriptionLabel = Label(root, font=("Arial", 16))
descriptionLabel.pack()

# Execution
root.mainloop()