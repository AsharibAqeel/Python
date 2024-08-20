print("Enter lines :")

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

uppercase_lines = [line.upper() for line in lines]

for line in uppercase_lines:
    print(line)
