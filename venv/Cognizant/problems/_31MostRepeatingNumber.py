

def most_repeating(input1,input2)->int:
    max_count=0
    for i in range(input1):
        count=0
        for j in range(input1):
            if input2[i] == input2[j]:
                count+=1
        if count > max_count:
            max_count = count
            number = input2[i]
    return number

size = int(input())
nums = list(map(int,input().split()))
print(most_repeating(size,nums))