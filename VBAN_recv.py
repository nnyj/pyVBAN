from pyVBAN import VBAN_Recv
import time

while True:
    try:
        # outDeviceIndex = -1 (Default output device)
        cl = VBAN_Recv("127.0.0.1","Stream1",6980,-1,verbose=False)
        cl.runforever()
    except:
        print('Crashed. Retrying in 1 second...')
        time.sleep(1)
        continue
