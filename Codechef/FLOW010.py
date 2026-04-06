t =int(input())
d = {
"b":"BattleShip",
"B":"BattleShip",
"c":"Cruiser",
"C":"Cruiser",
"d":"Destroyer",
"D":"Destroyer",
"f":"Frigate",
"F":"Frigate"
}
while t:
    t-=1
    print(d[input()])
