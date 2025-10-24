def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

func(1, 2, a=3, b=4)
# args: (1, 2)
# kwargs: {'a': 3, 'b': 4}
