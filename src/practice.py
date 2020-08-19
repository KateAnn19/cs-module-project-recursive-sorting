def print_num():
    print("*")

x = 3
count = 0
astricks = ""

while count < x:
    count += 1
    astricks += "*"
    if(count == x):
        astricks += '\n'
        x -= 1
        count = 0   


print(astricks)
