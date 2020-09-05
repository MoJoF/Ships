class WeaponsAndResources:
    def __init__(self, name, ship_type="Канонерка"):
        self.name = name
        self.ship_type = ship_type

        self.count_guns = 0
        self.count_falcos = 0
        self.count_shrap = 0
        self.count_mortires = 0
        self.count_fire_guns = 0
        self.greak_fire = 0

        # Resources
        self.gold = 1000
        self.iron = 100
        self.oil = 20
        self.food = 200
        self.rom = 0
        self.silk = 0
        self.powder = 200
        self.wood = 200

        if ship_type == 'Канонерка':
            # Access

            self.guns = True
            self.falco = False
            self.shrap = False
            self.fire_guns = False
            self.mortires = False
            self.greak_fire = False

            self.count_guns = 20

        elif ship_type == 'Шхуна':
            # Access

            self.guns = True
            self.falco = True
            self.shrap = False
            self.fire_guns = False
            self.mortires = False
            self.greak_fire = False

            # Count

            self.count_guns = 25
            self.count_falcos = 15

        elif ship_type == 'Галера':
            # Access

            self.guns = True
            self.falco = True
            self.shrap = True
            self.fire_guns = False
            self.mortires = False
            self.greak_fire = False

            # Count

            self.count_guns = 30
            self.count_falcos = 20
            self.count_shrap = 5

        elif ship_type == 'Фрегат':
            # Access

            self.guns = True
            self.falco = True
            self.shrap = True
            self.fire_guns = True
            self.mortires = False
            self.greak_fire = False

            # Count

            self.count_guns = 40
            self.count_falcos = 25
            self.count_shrap = 10
            self.count_fire_guns = 20

        elif ship_type == 'Линкор':
            # Access

            self.guns = True
            self.falco = True
            self.shrap = True
            self.fire_guns = True
            self.mortires = True
            self.greak_fire = False

            # Count

            self.count_guns = 50
            self.count_falcos = 30
            self.count_shrap = 15
            self.count_fire_guns = 25
            self.count_mortires = 10

        elif ship_type == 'Линейный корабль':
            # Access

            self.guns = True
            self.falco = True
            self.shrap = True
            self.fire_guns = True
            self.mortires = True
            self.greak_fire = True

            # Count

            self.count_guns = 55
            self.count_falcos = 35
            self.count_shrap = 20
            self.count_fire_guns = 30
            self.count_mortires = 15

