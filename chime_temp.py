import time
import serial
import json
import requests
# Team 
webhook_id = 'your_webhook_id'
WEBHOOK_URI = 'https://hooks.chime.aws/incomingwebhooks/' + webhook_id
ser = serial.Serial('/dev/cu.usbserial-14130', 9600)

def post_message(msg):
    response = None
    try:
        response = requests.post(
            url=WEBHOOK_URI,
            json={"Content": msg})
        return json.loads(response.text)
    except:
        return response.text

while True:
    temp = ser.readline()
    ser.flushInput()

    msg = "Current temperature is {} celsius. ".format(str(temp.strip(),'utf-8'))

    if float(temp.strip()) > 20:
        msg += "You can wear a singlet!"
    else:
        msg += "Remember to put on your jacket!"

    post_message(msg)
    time.sleep(2)
