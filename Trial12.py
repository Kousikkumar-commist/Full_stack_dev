choice=input("Enter your choice: ")
market={
    "stationary":{
        "Solids":{
            "extra":{
                "Glue gun":200
            },
            "Clay":40,
            "Sketch":30,
            "Paint":50
        },
        "pen":10,
        "pencil":5,
        "A4 sheet":1,
        "Geomentry box":50,
        "Bril Ink":35,
        "Pen stand":20
    },
    "Elecronics":{
        "Resistor":3,
        "transistor":4,
        'LED':5,
        "Arduino UNO":350,
        "Arduino NANO":250,
        "Bread Board":200
    },
    "Snacks":{
        "Chips":10,
        "Cookies":20,
        "Juice":15,
        'Chocolate':10 or 20,
    }
}
print(market["stationary"]["Solids"]["extra"]["Glue gun"])