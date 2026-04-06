def is_int(a):
    return int(a) == a

def converter(numero, base):
    resultado = 0
    mult = 0
    for digito in reversed(numero):
        valor = 0

        if digito.isdigit():
            valor = int(digito)
        elif digito.isalpha():
            valor = ord(digito.upper()) - ord('A') + 10
        if valor > base:
            raise ValueError("No es la base")
        elif base == 1 and valor == 1:
            pass
        elif base == 1 and valor == 0:
            raise ValueError("No es la base")
        elif base == valor:
            raise ValueError("No es la base")
        resultado += valor * base ** mult
        mult += 1

    return resultado

def eval(expr):
    ans = list()
    expr = list(expr.split(" "))
    for base in range(1, 37):
        try:
            a = converter(expr[0], base)
            b = converter(expr[2], base)
            c = converter(expr[4], base)
            if is_int(a) and is_int(b) and is_int(c):
                if expr[1] == "+":
                    result = a + b
                elif expr[1] == "-":
                    result = a - b
                elif expr[1] == "*":
                    result = a * b
                else:
                    result = a / b
                if result == c:
                    ans.append(base)
        except ValueError:
            pass
    ans = sorted(ans)
    return ans


base_dic = "123456789abcdefghijklmnopqrstuvwxyz0"
t = int(input())
while t:
    t-=1
    ans = eval(input())
    if len(ans) == 0:
        print("invalid")
    else:
        out_str = ""
        for elem in ans:
            out_str += base_dic[elem - 1]
        print(out_str)