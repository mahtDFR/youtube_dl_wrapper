import subprocess
import time

while True:
    x = input("paste video url to download or press (q) to quit. \n")
    if x == 'q':
        break
    else:
        command = "youtube-dl " + str(x)

        print("downloading video from source: " + str(x))
        time.sleep(1)

        subprocess.call((command), shell=True)

        print("done.")