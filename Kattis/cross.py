def check_row(row):
    s = set(row)
    if 0 in s:
        s.remove(0)
    possible = set(list(range(1,10)))
    for elem in s:
        if elem in possible:
            possible.remove(elem)
    return possible

def get_row(mat, i, j):
    ans = list()
    for tj in range(9):
        if tj!= j:
            ans.append(mat[i][tj])
    return ans

def get_column(mat, i, j):
    ans = list()
    for ti in range(9):
        if ti != i:
            ans.append(mat[ti][j])
    return ans

def get_square(mat, i, j):
    sub_quadrant_x = i // 3
    sub_quadrant_y = j // 3
    ans = list()
    for ti in range(sub_quadrant_x * 3, (sub_quadrant_x + 1) * 3):
        for tj in range(sub_quadrant_y * 3, (sub_quadrant_y + 1) * 3):
            if ti == i and tj== j:
                continue
            ans.append(mat[ti][tj])
    return ans

def print_square(mat):
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                print(".", end="")
            else:
                print(mat[i][j], end="")
        print()

def found_pos(d, valid_pos, mat):
    ## square
    sub_quadrant_x = valid_pos[0] // 3
    sub_quadrant_y = valid_pos[1] // 3
    s_list = list()
    for i in range(sub_quadrant_x * 3, (sub_quadrant_x + 1) * 3):
        for j in range(sub_quadrant_y * 3, (sub_quadrant_y + 1) * 3):
            if (i,j) != valid_pos and mat[i][j] == 0:
                s_list.append(d[(i,j)])
    ans1 = d[valid_pos]
    for elem in s_list:
        ans1 = ans1.difference(elem)
    if len(ans1) == 0:
        return False, ans1
    elif len(ans1) == 1:
        return True, ans1
    return False, ans1

def main():
    mat = list()
    for i in range(9):
        mat.append(input())
        mat[-1] = list(c for c in mat[-1])
        for j in range(9):
            if mat[-1][j] == '.':
                mat[-1][j] ='0'
            mat[-1][j] = int(mat[-1][j])

    op = True
    first_time = True
    while op:
        op = False
        
        d = {}
        for i in range(9):
            for j in range(9):
                row = get_row(mat, i, j)
                col = get_column(mat, i, j)
                square = get_square(mat, i, j)
                set_row = check_row(row)
                set_col = check_row(col)
                set_square = check_row(square)
                d[(i,j)] = set_row.intersection(set_col).intersection(set_square)
        
        for i in range(9):
            for j in range(9):
                if mat[i][j] != 0:
                    temp = mat[i][j]
                    __, s = found_pos(d, (i,j), mat)
                    if temp in s:
                        if len(s) == 2:
                            print("ERROR")
                            return
                        continue
                    else:
                        print("ERROR")
                        return
                
        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0:
                    founded, val = found_pos(d, (i,j), mat)
                    if founded:
                        mat[i][j] = list(val)[0]
                        op = True
                        break
            if op:
                break
    
    print_square(mat)


if __name__ == "__main__":
    main()