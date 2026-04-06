from sys import stdin, stdout 
import math
s = stdin.readline()
line_pos = dict()
line_list = list()
var_dict = dict()
pos = 0
MIN_VAL = -2147483648
MAX_VAL = 2147483647

def keep_range(valor):
    return (valor - MIN_VAL) % (MAX_VAL - MIN_VAL + 1) + MIN_VAL

def parse_(sub_line):
    ans = 0
    if sub_line[0] in var_dict  :
        ans = var_dict[sub_line[0]]
    elif sub_line[0].isdigit():
        ans = int(sub_line[0])
    try:
        op = sub_line[1]

        if op in ["+", "-", "*", "/"]:
            if op == "+":
                ans += parse_(sub_line[2:])
            elif op == "-":
                ans -= parse_(sub_line[2:])
            elif op == "*":
                ans *= parse_(sub_line[2:])
            else:
                temp = parse_(sub_line[2:])
                if ans * temp >= 0:
                    ans = ans // temp
                else:
                    ans = int(math.ceil(ans / temp))
    except:
        pass
    ans = keep_range(ans)
    return ans

def let_(sub_line):
    var_dict[sub_line[0]] = parse_(sub_line[2:])

def if_(sub_line):
    left = parse_(sub_line)
    for i in range(1, len(sub_line)):
        if sub_line[i] in ["=", ">", "<", "<>", "<=", ">="]:
            break
    sign = sub_line[i]
    right = parse_(sub_line[i + 1:])
    if sign == "=":
        is_true = left == right
    elif sign == "<":
        is_true = left < right
    elif sign == ">":
        is_true = left > right
    elif sign == "<=":
        is_true = left <= right
    elif sign == ">=":
        is_true = left >= right
    elif sign == "<>":
        is_true = left != right
        
    if is_true:
        return int(sub_line[-1])
    return -1

def print_(sub_line, new_line):
    if sub_line[0][0] == '"':
        prompt = " ".join(sub_line)[1:-1]
    else:
        prompt = var_dict[sub_line[0]]
    if new_line:
        print(prompt)
    else:
        print(prompt, end="")

def execute_line(sub_line):
    if sub_line[0] == "LET":
        let_(sub_line[1:])
    elif sub_line[0] == "IF":
        goto_ = if_(sub_line[1:])
        return goto_
    elif sub_line[0] == "PRINT":
        print_(sub_line[1:], new_line=False)
    else:
        print_(sub_line[1:], new_line=True)
    return -1

while s:
    if s == "x\n":
        break
    line = list(s.split())
    line_list.append(line)
    line_list[-1][0] = int(line_list[-1][0])
    pos += 1
    s = stdin.readline()

i = 0
line_pos_inverse = dict()
for elem in line_list:
    line_pos[elem[0]] = i
    line_pos_inverse[i] = elem[0]
    i += 1

j = line_pos_inverse
while j <= len(line_list) * 10:
    goto_ = execute_line(line_list[line_pos[j]][1:])
    if goto_ != -1:
        j = goto_
    else:
        j += 10

