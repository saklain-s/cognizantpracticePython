def vowelsAndConsonants(s)->int:

    vowelCount=0
    consotant=0
    for ch in s:
        if ch.isalpha() and ch in "aieouAEIOU":
            vowelCount+=1
        elif ch.isalpha():
            consotant+=1
    return vowelCount, consotant

text = input().strip()
vowel, consonant = vowelsAndConsonants(text)
print(f"Vowels:{vowel}, Consonants:{consonant}")