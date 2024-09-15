import pyautogui
import time
import random
import keyboard  # Modul pro detekci klávesových stisků

while True:
    # Pokud je stisknuta klávesa 'q', skript se ukončí
    if keyboard.is_pressed('q'):
        print("Program ukončen uživatelem.")
        break
    
    # Simulace stisknutí klávesy F5
    pyautogui.press('f5')
    
    # Čekání náhodný počet sekund mezi 5.0 a 9.0
    wait_time = random.uniform(5.0, 9.0)
    time.sleep(wait_time)
