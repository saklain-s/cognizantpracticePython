with open(r"C:\Users\User\OneDrive\Desktop\hub\C Programs\write.txt","r+") as f:
    f.write("Appending new line.\n")
    for line in f:
        print(line.strip())

with open(r"C:\Users\User\OneDrive\Desktop\hub\C Programs\data.txt","r") as f:
    for line in f:
        print(line.strip())