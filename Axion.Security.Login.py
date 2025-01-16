import os
import time

def clear_console():
  """Clears the console output."""
  if os.name == 'nt': 
    os.system('cls')  # For Windows
  else:
    os.system('clear')  # For macOS and Linux

print("""Axion Security services loading...""")
time.sleep(3)
print("Opening servers for login...")
time.sleep(5)
clear_console()  # Call clear_console() here

passcode = input("Input passcode:")
if passcode == "00.2008.00":
  print("Hello |name|. Welcome to the Axion Security Servers database. ")
else:
  print("Access Denied and system locked.")
  time.sleep(3)
  clear_console()

