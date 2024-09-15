import pyautogui
import time
import random
import threading

# Proměnná pro ukončení skriptu
running = True

# Funkce pro sledování vstupu uživatele
def listen_for_exit():
    global running
    input("Stiskni Enter pro ukončení programu...\n")
    running = False

# Vytvoření a spuštění vlákna pro sledování ukončení
exit_thread = threading.Thread(target=listen_for_exit)
exit_thread.start()

while running:
    # Simulace stisknutí klávesy F5
    pyautogui.press('f5')

    # Čekání náhodný počet sekund mezi 5.0 a 9.0
    wait_time = random.uniform(3.3, 7.4)
    time.sleep(wait_time)

print("Program ukončen.")
