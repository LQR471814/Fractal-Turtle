import turtle
import json
import argparse
import svgwrite
from SvgTurtle import SvgTurtle
import time


def write_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    t = SvgTurtle(drawing)
    turtle.Turtle._screen = t.screen
    turtle.Turtle._pen = t
    draw_func()
    drawing.save()

parser = argparse.ArgumentParser(description='Fractal Turtle v0.1.0')

#? Required

parser.add_argument("-s", "--settings", required=True, help="Ex. /path/to/your/fractal_settings.json")
parser.add_argument("-l", "--length", required=True, help="Ex. 10 px")
parser.add_argument("-i", "--iterations", required=True, help="Ex. 4")

#? Optional

parser.add_argument("-v", "--verbose", help="Ex. True")
parser.add_argument("-e", "--export", help="Ex. True")
parser.add_argument("-eH", "--export-scale-horizontal", help="Ex. 1280 px")
parser.add_argument("-eV", "--export-scale-vertical", help="Ex. 720 px")

args = parser.parse_args()

f = open(args.settings, "r")
options = json.loads(f.read())

turtle.left(90)

if str(args.verbose).lower() != "true":
    turtle.speed(0)
    turtle.hideturtle()

    turtle.tracer(0, 0)
else:
    turtle.speed(1)

class rule:
    def __init__(self, value, equation):
        self.equation = equation
        self.value = value

class state:
    def __init__(self, position, rotation):
        self.position = position
        self.rotation = rotation
    def load(self):
        turtle.penup()
        turtle.setposition(self.position[0], self.position[1])
        turtle.pendown()
        turtle.setheading(self.rotation)

def render(lString):
    global angle
    global length
    global axiom
    global line

    pendingLinks = []
    currentState = None

    for letter in lString:
        if letter in line:
            turtle.forward(length)
        elif letter == "-":
            turtle.left(angle)
        elif letter == "+":
            turtle.right(angle)
        elif letter == "[":
            pendingLinks.append(state(position=turtle.position(), rotation=turtle.heading()))
        elif letter == "]":
            pendingLinks[-1].load()
            pendingLinks.pop(-1)

def fractal(lString, rules):
    global length

    constants = ["+", "-", "[", "]"]

    for i in range(iterations):
        newString = ""
        for letter in lString:
            if letter in constants:
                newString += letter
                continue
            for rule in rules:
                if letter == rule.value:
                    newString += rule.equation

        lString = newString

    render(lString)

scaleV = args.export_scale_vertical
scaleH = args.export_scale_horizontal

if args.export == "True" or args.export == "False":
    export = bool(args.export)
else:
    export = args.export

angle = options["angle"]
length = float(args.length)
axiom = options["axiom"]
line = options["line"]
iterations = int(args.iterations)

def main():
    rules = options["rules"]
    for val, i in zip(rules, range(len(rules))):
        rules[i] = rule(value=val["value"], equation=val["equation"])

    time1 = time.time()
    fractal(axiom, rules)
    time2 = time.time()
    print("Finished processing in " + str(round(time2 - time1, 2)) + "s" + "!")

if export != True:
    main()
    turtle.update()

    turtle.mainloop()
else:
    if scaleH != None and scaleV != None:
        write_file(main, 'fractal.svg', size=(scaleH + "px", scaleV + "px"))
        print("Exported!")
    else:
        write_file(main, 'fractal.svg', size=("10000px", "10000px"))
        print("Exported!")