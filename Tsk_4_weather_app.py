import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your Weatherbit API key
API_KEY = "036fdf52e1d64d6ab5bf53be8556a8cf"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")

        self.city_label = tk.Label(root, text="Enter city name:", font=("Arial", 14))
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root, font=("Arial", 14))
        self.city_entry.pack(pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=self.get_weather)
        self.get_weather_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill='both')

        self.weather_label = tk.Label(root, text="", font=("Arial", 16))
        self.weather_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        try:
            base_url = "https://api.weatherbit.io/v2.0/current"
            params = {
                "city": city,
                "key": API_KEY,
            }

            response = requests.get(base_url, params=params)
            data = response.json()

            if "data" in data:
                temperature = data["data"][0]["temp"]
                description = data["data"][0]["weather"]["description"]

                weather_info = f"Weather in {city}:"
                weather_info += f"\nTemperature: {temperature}°C"
                weather_info += f"\nDescription: {description}"

                self.weather_label.config(text=weather_info)
            else:
                messagebox.showerror("Error", "City not found or data not available. Please check your input.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.geometry("400x400")  # Set the window size
    root.mainloop()
