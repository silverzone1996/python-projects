class auto:
    def __init__(self, farbe, marke):
        self.farbe =farbe
        self.marke = marke


    def fahren(self):
        print(f"Das auto der marke {self.marke} hat die farbe {self.farbe}")


auto1=auto("grün", "vw")
auto1.fahren()