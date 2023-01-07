values = [1, 2, '3', 'forth', 'end', 99, True, None]
mapped_numbers = list(map(lambda x:str(x) if type(x)==int else x,values))
print(mapped_numbers)

