n = 28
n = list(n)
n.reverse()
decimal = 0
for i in range(len(n)):
    decimal += int(n[i]) * 2 ** i
print(decimal)

