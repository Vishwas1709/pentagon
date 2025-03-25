class Fan:
    def __init__ (self):
        self.brand="usha"
        self.cost=3000
        self.color="white"
        self.numofBlades=3
        
    def on(self):
        print("The fan is ON")
    def rotate(self):
        print("The fan is rotate")
    def off(self):
        print("the fan is off")
f1=Fan()
print(f1.brand)
print(f1.cost)
print(f1.color)
print(f1.numofBlades)
f1.on()
f1.rotate()
f1.off()