class heroes : # Template
    pass
# object
hero1 = heroes()
hero2 = heroes()
hero3 = heroes()

hero1.name = "sniper"
hero1.health = 200

hero2.name = "sven"
hero2.health = 300

hero3.name = "akai"
hero3.health = 500

print(hero1.__dict__)
print("the first heroes name is " + hero1.name)
print("the first heroes health is ", hero1.health)
print("-" * 30 )
print(hero2.__dict__)
print("-"*30)
print(hero3.__dict__)