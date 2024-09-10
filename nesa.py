import time
import random
from datetime import datetime
import pyautogui
import pyperclip

# Funkce, kterou chceš volat opakovaně
def moje_funkce():
    print("Funkce !work byla zavolána v", datetime.now())
    pyautogui.moveTo(1678, 475, duration=0.3)
    pyautogui.doubleClick()
    # Používá clipboard pro vložení textu
    pyperclip.copy("!work")
    pyautogui.hotkey('ctrl', 'v')  # Používá Ctrl + V pro vložení textu

# Funkce, která se má volat jednou denně při vstupu do povoleného času
def daily():
    print("Funkce !daily byla zavolána v", datetime.now())
    pyautogui.moveTo(1678, 475, duration=0.3)
    pyautogui.click()
    # Používá clipboard pro vložení textu
    pyperclip.copy("!daily")
    pyautogui.hotkey('ctrl', 'v')  # Používá Ctrl + V pro vložení textu

# Funkce, která se volá, když je časový interval menší než 61 minut
def znovu():
    print("Funkce znovu() byla zavolána, protože interval byl menší než 61 minut.")
    time.sleep(random.uniform(17.0, 30.0) * 60)
    moje_funkce()

# Kontroluj, zda je aktuální čas v povoleném rozmezí
def je_povoleny_cas():
    nyni = datetime.now().time()
    start_cas = datetime.strptime("08:00", "%H:%M").time()
    konec_cas = datetime.strptime("02:00", "%H:%M").time()

    if start_cas <= nyni <= konec_cas or (start_cas > konec_cas and (nyni >= start_cas or nyni <= konec_cas)):
        return True
    return False

# Hlavní smyčka
def spustit_funkci_v_nahodnych_intervalech():
    daily_called = False  # Sleduj, zda byla funkce daily() zavolána
    while True:
        # Zkontroluj, zda je aktuální čas povolený
        if je_povoleny_cas():
            # Vygeneruj náhodný časový interval (45 až 93 minut)
            dalsi_cas_minuty = random.uniform(45.0, 93.0)
            print(f"Další volání bude za {dalsi_cas_minuty} minut.")
            # Uspi skript na daný počet minut
            time.sleep(dalsi_cas_minuty * 60)
            # Zavolej funkci daily(), pokud ještě nebyla zavolána
            if not daily_called:
                daily()
                daily_called = True  # Nastav příznak, že daily() byla zavolána

            # Zavolej hlavní funkci
            moje_funkce()

            # Pokud je interval menší než 61 minut, zavolej funkci znovu()
            if dalsi_cas_minuty < 61:
                znovu()
        else:
            # Pokud je mimo časové okno, resetuj příznak daily()
            daily_called = False
            # Pokud je mimo časové okno, počkej 10 minut a zkontroluj znovu
            print("Mimo povolený čas, čekám 10 minut.")
            time.sleep(10 * 60)

# Spusť smyčku
spustit_funkci_v_nahodnych_intervalech()
