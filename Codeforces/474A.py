firsto = "qwertyuiop"
secando = "asdfghjkl;"
sado = "zxcvbnm,./"
option = input()
message = input()
ans = ""
if option == "L":
    skiper = 1
else:
    skiper = -1
for letter in message:
    f,s,sad = firsto.find(letter), secando.find(letter), sado.find(letter)
    if f != -1:
        ans += firsto[f + skiper]
    elif s != -1:
        ans += secando[s + skiper]
    else:
        ans += sado[sad + skiper]
print(ans)
