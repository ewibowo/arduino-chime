import time
import serial
import json
import requests
# Team Calendar
WEBHOOK_URI = 'https://hooks.chime.aws/incomingwebhooks/8e8b4f67-10b3-4ab6-b9a8-d4b65f48a1fd?token=dk5WblczUG18MXxlRWhEU0tKdk12ekQtbG0zSDZNeXhlRFh3UVlFZU84clBJaXl1TUpoTnNR'

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
