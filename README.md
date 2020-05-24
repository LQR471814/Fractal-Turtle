# Fractal-Turtle

A python turtle program that can render fractals using L-Systems. Customization is handled with .json files and there are a few presets included.

## Command Line Arguments

### **Required**

#### `-s | --settings Ex. ./presets/plants/seaweed.json`

Path to your fractal configuration JSON file.

### **With Defaults**

#### `-l | --length Default: 20`

Length of each line drawn

#### `-i | --iterations Default: 5`

The number of fractal iterations

#### `-eH | --export-scale-horizontal Default: 10000`

Specify the horizontal scale of the .svg file (Yes this is a thing)

#### `-eV | --export-scale-vertical Default: 10000`

Specify the horizontal scale

### **Optional**

#### `-e | --export Ex. True`

Export the fractal as an .svg file

#### `-v | --verbose Ex. True`

Enable debugging

## L-System Configuration Files

Using configuration files one can create custom fractals in the format of L-Systems and render them with Fractal Turtle.

JSON Format

```JSON
{
    "line":["F"],
    "axiom":"F--F--F",
    "angle":60,
    "rules":[
        {"value":"F", "equation":"F+F--F+F"}
    ]
}
```

Example from `snowflake.json`

The `line` array defines which variables will make the turtle draw a line.

The `axiom` string defines the starting value of the fractal.

The `angle` integer defines the angle left or right at each turn.

The `rules` array holds the rules that the fractal will follow.

Each map inside of the `rules` array has a key named value and a key named equation. Value holds the value that will be replaced by the equation every iteration.

## External Dependencies

svgwrite - <https://pypi.org/project/svgwrite/>
