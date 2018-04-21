import io

x = input()
result = ""
for i in range(1, 4):
    file = None
    if i == 1:
        file = io.open(x + ".txt", encoding="utf8")
    else:
        file = io.open(x + str(i) + ".txt", encoding="utf8")
    result += file.read() + "\n"
bw = open(x + "_all.txt", "w", encoding="utf8")
bw.write(result)
bw.close()
print(result)
