tc = int(input())
for __ in range(tc):
    for ___ in range(3):
        line = input()
        db = set()
        for elem in line:
            db.add(elem)
        if "?" in db:
            if "A" in db and "B" in db:
                print("C")
            elif "B" in db and "C" in db:
                print("A")
            else:
                print("B")
    