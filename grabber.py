import sys
from time import sleep
import pyscreenshot
import keyboard
import os
import errno
if __name__ == '__main__':

    directory = "images"

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("RACE condition on creating image dir")
                exit(1)

    print("Waiting 10 seconds to start process. Please Fullscreen Window to grab")
    sleep(10)

    pages = int(sys.argv[1])

    imgname = "currentscreen.png"

    for i in range(0, pages):
        im = pyscreenshot.grab()
        try:
            im.save(imgname+"page{}".format(i))
        except Exception as e:
            print("Error at saving file. Try running as administrator.")

        keyboard.press_and_release("right")

        sleep(3)

    print("Finished.")
    exit(0)