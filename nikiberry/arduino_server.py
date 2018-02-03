from flask import Flask
import serial

app = Flask(__name__)

ser = serial.Serial("/dev/ttyACM1", 9600, timeout=0)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/start_motor")
def start_motor():
    ser.write("1")
    return "motor started"
    
@app.route("/stop_motor")
def stop_motor():
    ser.write("0")
    return "motor stopped"
    
app.run(host='0.0.0.0')

