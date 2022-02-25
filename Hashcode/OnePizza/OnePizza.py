from os import listdir
from os.path import isfile, join
mypath = "input_data"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file_name in onlyfiles:
    with open(f"{mypath}/{file_name}", 'r') as f:
        tc = int(f.readline())
        m = {}
        while tc:
            tc-=1
            #recommended
            r = f.readline().split()
            for i in range(1, len(r)):
                if r[i] in m:
                    m[r[i]] += 1
                else:
                    m[r[i]] = 1

            #not recommended
            nr = f.readline().split()
            for i in range(1, len(nr)):
                if nr[i] in m:
                    m[nr[i]] -= 1
                else:
                    m[nr[i]] = -1

        ingredients = 0
        for value in m.values():
            if value > 0:
                ingredients += 1
        with open(f"{file_name[0]}_out.txt", "w") as out_file:
            out_file.write(str(ingredients) + " " + " ".join([key for key, value in m.items() if value > 0]))
