import pyttsx3
import tkinter as tk

# Initialize Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Create main window
window = tk.Tk()
window.title("Assistive Communication System")
window.geometry("400x400")

# Title label
title = tk.Label(window, text="Select a Symbol", font=("Arial", 16))
title.pack(pady=10)

# Buttons
btn_food = tk.Button(window, text="🍔 Food", font=("Arial", 14),
                     command=lambda: speak("I want food"))
btn_food.pack(pady=5)

btn_water = tk.Button(window, text="💧 Water", font=("Arial", 14),
                      command=lambda: speak("I want water"))
btn_water.pack(pady=5)

btn_toilet = tk.Button(window, text="🚻 Toilet", font=("Arial", 14),
                       command=lambda: speak("I need to use the toilet"))
btn_toilet.pack(pady=5)

btn_help = tk.Button(window, text="🆘 Help", font=("Arial", 14),
                     command=lambda: speak("Please help me"))
btn_help.pack(pady=5)

btn_happy = tk.Button(window, text="😊 Happy", font=("Arial", 14),
                      command=lambda: speak("I am happy"))
btn_happy.pack(pady=5)

# Run the window
window.mainloop()
