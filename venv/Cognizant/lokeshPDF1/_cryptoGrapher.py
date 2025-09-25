text = input()
new_text = ""
for ch in text:
    if ch == 'a':
        new_text += 'z'
    elif ch == 'A':
        new_text += 'Z'
    else:
        new_text += chr(ord(ch)-1)
print(new_text)