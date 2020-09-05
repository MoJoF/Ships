class DamageWeaponShip:
    def __init__(self, name, ship_type='Канонерка'):
        self.name = name
        self.ship_type = ship_type

        if self.ship_type == 'Канонерка':
            # Health

            self.bushprit = 50
            self.fok = 80
            self.grot = 90
            self.bizan = 120

            # Weapon
            # Gun
            # Count

            self.bushprit_guns = 1
            self.fok_guns = 2
            self.grot_guns = 4
            self.bizan_guns = 6

            # Dmg Gun
            self.damage_one_gun = 3

        elif self.ship_type == 'Шхуна':
            # Health

            self.bushprit = 100
            self.fok = 160
            self.grot = 180
            self.bizan = 240

            # Weapon
            # Gun
            # Count

            self.bushprit_guns = 2
            self.fok_guns = 5
            self.grot_guns = 7
            self.bizan_guns = 8

            # Dmg Gun
            self.damage_one_gun = 3

            # Falco

            self.fok_falcos = 2
            self.grot_falcos = 2
            self.bizan_falcos = 4

            # Dmg Falco

            self.damage_one_falco = 1

            self.damage_one_falco_crit = 10

        elif self.ship_type == 'Галера':
            # Health

            self.bushprit = 200
            self.fok = 320
            self.grot = 360
            self.bizan = 480

            # Weapon
            # Gun
            # Count

            self.bushprit_guns = 4
            self.fok_guns = 7
            self.grot_guns = 9
            self.bizan_guns = 10

            # Dmg Gun
            self.damage_one_gun = 4

            # Falco

            self.fok_falcos = 2
            self.grot_falcos = 4
            self.bizan_falcos = 7

            # Dmg Falco

            self.damage_one_falco = 1

            self.damage_one_falco_crit = 12

            # Shrapnel

            self.damage_shrap = 100

        elif self.ship_type == 'Фрегат':
            # Health

            self.bushprit = 400
            self.fok = 640
            self.grot = 720
            self.bizan = 960

            # Weapon
            # Gun
            # Count

            self.bushprit_guns = 5
            self.fok_guns = 9
            self.grot_guns = 11
            self.bizan_guns = 13

            # Dmg Gun
            self.damage_one_gun = 4

            # Falco

            self.fok_falcos = 3
            self.grot_falcos = 7
            self.bizan_falcos = 10

            # Dmg Falco

            self.damage_one_falco = 2

            self.damage_one_falco_crit = 15

            # Shrapnel

            self.damage_shrap = 100

            # Fire Guns

            self.bushprit_fire_guns = 5
            self.fok_fire_guns = 9
            self.grot_fire_guns = 11
            self.bizan_fire_guns = 13

            # Dmg Fire Gun

            self.damage_one_fire_gun = 6

        elif self.ship_type == 'Линкор':
            # Health

            self.bushprit = 800
            self.fok = 1280
            self.grot = 1440
            self.bizan = 1920

            # Weapon
            # Gun
            # Count

            self.bushprit_guns = 7
            self.fok_guns = 12
            self.grot_guns = 15
            self.bizan_guns = 18

            # Dmg Gun
            self.damage_one_gun = 4

            # Falco

            self.fok_falcos = 5
            self.grot_falcos = 9
            self.bizan_falcos = 11

            # Dmg Falco

            self.damage_one_falco = 3

            self.damage_one_falco_crit = 17

            # Shrapnel

            self.damage_shrap = 100

            # Fire Guns

            self.bushprit_fire_guns = 7
            self.fok_fire_guns = 12
            self.grot_fire_guns = 15
            self.bizan_fire_guns = 18

            # Dmg Fire Gun

            self.damage_one_fire_gun = 7

            # Mortires

            self.grot_mortires = 1
            self.bizan_mortires = 4

            # Dmg Mortire

            self.damage_one_mortire = 50

        elif self.ship_type == 'Линейный корабль':
            # Health

            self.bushprit = 1600
            self.fok = 2560
            self.grot = 2880
            self.bizan = 3840

            # Weapon
            # Gun
            # Count

            self.bushprit_guns = 8
            self.fok_guns = 13
            self.grot_guns = 17
            self.bizan_guns = 20

            # Dmg Gun
            self.damage_one_gun = 5

            # Falco

            self.fok_falcos = 7
            self.grot_falcos = 11
            self.bizan_falcos = 12

            # Dmg Falco

            self.damage_one_falco = 4

            self.damage_one_falco_crit = 18

            # Shrapnel

            self.damage_shrap = 100

            # Fire Guns

            self.bushprit_fire_guns = 8
            self.fok_fire_guns = 13
            self.grot_fire_guns = 17
            self.bizan_fire_guns = 20

            # Dmg Fire Gun

            self.damage_one_fire_gun = 8

            # Mortires

            self.grot_mortires = 3
            self.bizan_mortires = 6

            # Dmg Mortire

            self.damage_one_mortire = 55

            # Greak Fire

            self.damage_greak_fire = 100

    def health(self):
        health = self.bushprit + self.fok + self.grot + self.bizan
        return health

    def damage_gun(self):
        guns_count = self.bushprit_guns + self.fok_guns + self.grot_guns + self.bizan_guns
        damage_guns = self.damage_one_gun * guns_count
        return damage_guns

    def damage_falco(self):
        falco_count = self.fok_falcos + self.grot_falcos + self.bizan_falcos
        damage_falcos = self.damage_one_falco * falco_count
        return damage_falcos

    def damage_falco_crit(self):
        falco_count = self.fok_falcos + self.grot_falcos + self.bizan_falcos
        damage_falcos_crit = self.damage_one_falco_crit * falco_count
        return damage_falcos_crit

    def damage_fire_gun(self):
        fire_gun_count = self.bushprit_fire_guns + self.fok_fire_guns + self.grot_fire_guns + self.bizan_fire_guns
        damage_fire_guns = self.damage_one_fire_gun * fire_gun_count
        return damage_fire_guns

    def damage_mortire(self):
        mortire_count = self.grot_mortires + self.bizan_mortires
        damage_mortire = self.damage_one_mortire * mortire_count
        return damage_mortire
