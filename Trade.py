class Trade:
    def __init__(self, gold, oil, powder, iron, food, wood, silk, rom):
        self.gold = gold
        self.oil = oil
        self.powder = powder
        self.iron = iron
        self.food = food
        self.wood = wood
        self.silk = silk
        self.rom = rom

    def food_gold(self):
        self.gold -= 50
        self.food += 5

    def iron_gold(self):
        self.gold -= 150
        self.iron += 5

    def oil_gold(self):
        self.gold -= 200
        self.oil += 5

    def wood_gold(self):
        self.gold -= 75
        self.wood += 5

    def rom_gold(self):
        self.gold -= 200
        self.rom += 5

    def silk_gold(self):
        self.gold -= 50
        self.silk += 5

    def powder_gold(self):
        self.gold -= 80
        self.powder += 5
