def operate(cache):
    return int(eval(cache))

def eval_expression(t):
    cache_base = "4"
    operations = ["+", "-", "*", "//"]
    for op_1 in operations:
        cache_1 = cache_base + op_1 + "4"
        for op_2 in operations:
            cache_2 = cache_1 + op_2 + "4"
            for op_3 in operations:
                cache_final = cache_2 + op_3 + "4"
                result = operate(cache_final)
                if result == t:
                    cache_final = cache_final.replace("//", "/")
                    final_answer = ""
                    for elem in cache_final:
                        final_answer += elem + " "
                    final_answer += f"= {t}"
                    return final_answer
    return "no solution"

m = int(input())
while m:
    m-=1
    t = int(input())
    print(eval_expression(t))