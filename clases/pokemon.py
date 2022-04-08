class Pokemon():

    def __init__(self, id, name, type, hp, attack, defense):
        id = id
        name = name
        type = type
        hp = hp
        attack = attack
        defense = defense
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        if self.hp == 0:
            return False
        else:
            return True

    def fight_defense(self, pokemon1, pokemon2):
        while True:
            turno = input('¿A qué pokemon le toca atacar?(1/2)')
            try:
                turno == 1 or turno ==2
            except:
                pass
            else:
                break
        if turno == 1:
            if pokemon1.self.attack < pokemon2.self.defense:
                return False
            else:
                return True
        
    def fight_attack(self, pokemon1, pokemon2):
        if self.fight_defense == False:
            return False
        else:
            pokemon2.self.hp = pokemon2.self.hp - (pokemon1.self.attack - pokemon2.self.defense)