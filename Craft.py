class Craft:
    def __init__(self, gold, oil, powder, iron, food, wood, silk, rom,
                 count_guns, count_fire_guns, count_falcos, count_mortires, count_shrap, greak_fire):
        self.gold = gold
        self.oil = oil
        self.powder = powder
        self.iron = iron
        self.food = food
        self.wood = wood
        self.silk = silk
        self.rom = rom

        self.count_guns = count_guns
        self.count_fire_guns = count_fire_guns
        self.count_falcos = count_falcos
        self.count_mortires = count_mortires
        self.count_shrap = count_shrap
        self.greak_fire = greak_fire


    def craft_kernels_x10(self):
        if (self.iron < 10 or self.gold < 20):
            return "Недостаточно ресурсов"
        else:
            self.iron -= 10
            self.gold -= 20
            self.count_guns += 10

    def craft_fire_kernels_x10(self):
        if (self.iron < 10 or self.gold < 30 or self.oil < 10):
            return "Недостаточно ресурсов"
        else:
            self.iron -= 10
            self.gold -= 30
            self.oil -= 10
            self.count_fire_guns += 10

    def craft_falco_kernels_x10(self):
        if (self.gold < 15 or self.iron < 5):
            return "Недостаточно ресурсов"
        else:
            self.gold -= 15
            self.iron -= 5
            self.count_falcos += 10

    def craft_mortire_kernels(self):
        if (self.gold < 100 or self.iron < 20):
            return "Недостаточно ресурсов"
        else:
            self.gold -= 100
            self.iron -= 20
            self.count_mortires += 10

    def craft_shrap(self):
        if (self.iron < 5 or self.gold < 10):
            return "Недостаточно ресурсов"
        else:
            self.iron -= 5
            self.gold -= 10
            self.count_shrap += 1

    def craft_greak_fire(self):
        if (self.wood < 10 or self.oil < 5 or self.gold < 50):
            return "Недостаточно ресурсов"
        else:
            self.wood -= 10
            self.oil -= 5
            self.gold -= 50
            self.greak_fire += 1