def gen_numbers(n):
    for i in range(n):
        yield i

for num in gen_numbers(3):
    print(num)  # 0,1,2
