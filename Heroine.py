class Heroine:
    def __init__(self):
        self.name="Ramya"
        self.age=45
        self.noofMovie=38
    def act(self):
        print("Ramya is a actress")
h1=Heroine()
print(h1.name)
print(h1.age)
print(h1.noofMovie)
h1.act()
h1.height=5.5
print(h1.height)
del h1.height
h1.age=50
print(h1.age)