def func(lst):
    return {a: lst.count(a) for a in set(lst) if lst.count(a) > 1}
print(func([1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,6,4,3,2,3,4,4,3,6,5,7,5,6,7,9,0,1,2,3]))

