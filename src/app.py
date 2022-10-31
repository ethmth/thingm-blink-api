from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from blink1.blink1 import Blink1


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

b1 = Blink1()

def rgb_to_hex(rgb):
    return "#" + str('%02x%02x%02x' % rgb)

def call_blink_function(method, color_value, transition_time=1000):
    if method == "fade":
        b1.fade_to_color(transition_time, color_value)
    if method == "blink":
        b1.write_pattern_line(transition_time, color_value, 1)
        b1.write_pattern_line(transition_time, '#000000', 2)
        b1.play(1,2)
    
    return


def handle_color(method, color_value, transition_time=1000):
    error_output = ""

    try:
        call_blink_function(method, color_value, transition_time)

        return f"Blink changed with color {color_value} with method {method}."
    except:
        pass
   
    try:
        tempval = color_value
        red_value = tempval[0:tempval.index(",")]
        tempval = tempval[(tempval.index(",") + 1): len(tempval)]
        green_value = tempval[0:tempval.index(",")]
        tempval = tempval[(tempval.index(",") + 1): len(tempval)]
        blue_value = tempval

        red_value = int(red_value)
        green_value = int(green_value)
        blue_value = int(blue_value)

        tempval = rgb_to_hex((red_value, green_value, blue_value))

        call_blink_function(method, tempval, transition_time)

        return f"Blink changed with rgb value ({red_value}, {green_value}, {blue_value}) with method {method}."
    except:
        pass

    try:
        hexval = color_value
        if len(hexval) == 7:
            hexval = hexval[1: len(hexval)]
        hexval = "#" + hexval

        call_blink_function(method, hexval, transition_time)

        return f"Blink changed with hex value {hexval} with method {method}."
    except:
        pass


    return f"You've provided an invalid color\n{error_output}"
    


@app.route("/")
@cross_origin()
def home():
    return f"To change the light color, query /fade. To have it blink, /blink. To turn it off, /off"


@app.route("/off")
@cross_origin()
def off():
    b1.off()
    return f"Blink turned off"

@app.route("/fade")
@cross_origin()
def fade():
    method = "fade"

    transition_time = request.args.get('time')
    if transition_time is not None:
        transition_time = int(transition_time)
    else:
        transition_time = 1000

    color_value = request.args.get('color')
    if color_value is None:
        return f"Please specify a color value. Example: /{method}?color=red or /{method}?color=5523f2 or /{method}?color=13,22,192. You can also specify an optional time argument."

    return handle_color(method, color_value, transition_time)

@app.route("/blink")
@cross_origin()
def blink():
    method = "blink"

    transition_time = request.args.get('time')
    if transition_time is not None:
        transition_time = int(transition_time)
    else:
        transition_time = 1000

    color_value = request.args.get('color')
    if color_value is None:
        return f"Please specify a color value. Example: /{method}?color=red or /{method}?color=5523f2 or /{method}?color=13,22,192. You can also specify an optional time argument."

    return handle_color(method, color_value, transition_time)
        

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")