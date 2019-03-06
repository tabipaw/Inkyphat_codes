
from flask import Flask, request
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

#API
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    with open("index.html") as f:
        indexpage = f.read()
    return indexpage

@app.route('/clean', methods=["GET"])
def clean():
    message = "Empty"
    r = update(message)

    return r

@app.route('/newdata', methods=["post"])
def newdata():
    name = request.form['name']
    email = request.form['email']
    maintext = request.form['maintext']
    maintext2 = request.form['maintext2']

    #pict = request.form['pict']
    r = update(name,email,maintext,maintext2)
    return r


#routines
def update(message,message2,message3,message4):

    #set param
    inky_display = InkyPHAT("yellow")
    inky_display.set_border(inky_display.WHITE)
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FredokaOne, 22)
    inky_display.set_border(inky_display.BLACK)

    x = 5
    y = 5
    y2= 25
    y3= 55
    y4= 75

    #write screen
    draw.text((x, y), message, inky_display.BLACK, font)
    draw.text((x, y2), message2, inky_display.BLACK, font)
    draw.text((x, y3), message3, inky_display.YELLOW, font)
    draw.text((x, y4), message4, inky_display.YELLOW, font)

    inky_display.set_image(img)
    inky_display.show()

    return message


#main
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

