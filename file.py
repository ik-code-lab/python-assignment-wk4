file = open("names.txt", "r")
print(file.read())
file.close()

file = open("names.txt", "a")
file.write("Yahoo")
file.close()

try:
    file = open("context.txt","r")
    print(file.read())
except:
    print("file doesnt exist")    