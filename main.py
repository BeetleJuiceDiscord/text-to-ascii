import os
import requests
import time


os.system("title Simple text to ASCII")


print("""

Simple text to ASCII | By King Herod

        Input text

""")

text = input(">")

convert = requests.get("http://artii.herokuapp.com/make?text=" + text)

log = open("ascii.txt", "w")
log.write(str(convert.text))
log.close()

print("Converted " + text + " to ASCII\n\nASCII has been logged in ascii.txt")


print("\n\n\nClosing in 10 seconds...")
time.sleep(10)
os.system("exit")
