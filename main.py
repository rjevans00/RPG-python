from classes.game import person, bcolours


magic = [{"name": "Fire", "cost" :10, "dmg": 60},
         {"name": "Thunder", "cost" :10, "dmg": 60},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]






player = person (460, 65, 34, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
