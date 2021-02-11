import psutil
import time
a = 0
while 1:
    a += 3.14

    print(psutil.cpu_percent(), psutil.virtual_memory().percent)
    time.sleep(.5)
    if a > 1000:
        break
