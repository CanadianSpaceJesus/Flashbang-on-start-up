import winreg
import random
import time
import pyautogui
import os
import sys

def add_to_startup(file_path):
    key = winreg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    key_value = "WhiteScreenApp"
    with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
        winreg.SetValueEx(reg_key, key_value, 0, winreg.REG_SZ, file_path)

def remove_from_startup():
    key = winreg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    key_value = "WhiteScreenApp"
    with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
        winreg.DeleteValue(reg_key, key_value)

def main():
    # Generate a random time between 11pm and 4am
    hours = random.randint(23, 23)  # 11pm to 11pm
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    random_time = time.strptime(f"{hours}:{minutes}:{seconds}", "%H:%M:%S")

    # Calculate the number of seconds until the random time
    current_time = time.localtime()
    current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
    random_seconds = random_time.tm_hour * 3600 + random_time.tm_min * 60 + random_time.tm_sec
    wait_seconds = random_seconds - current_seconds

    if wait_seconds < 0:
        wait_seconds += 24 * 3600  # Add 24 hours to get the next day

    # Wait until the random time
    time.sleep(wait_seconds)

    # Display a white screen for 1 second
    width, height = pyautogui.size()
    pyautogui.screenshot("white_screen.png")  # Take a screenshot
    white_screen = pyautogui.screenshot(region=(0, 0, width, height))  # Create a white screen image
    white_screen.save("white_screen.png")
    pyautogui.click(1, 1)  # Click to focus on the screen
    pyautogui.hotkey('win', 'd')  # Minimize all windows
    pyautogui.hotkey('win', 'd')  # Restore all windows
    pyautogui.hotkey('win', 'd')  # Minimize all windows again

    # Remove from startup
    remove_from_startup()

    # Exit the program
    sys.exit()

if __name__ == "__main__":
    # Add to startup
    script_path = os.path.abspath(sys.argv[0])
    add_to_startup(script_path)

    # Main loop
    while True:
        main()

