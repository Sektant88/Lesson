dict_old = {'abc':123, 'bcd':321, 'cde':456}
dict_new = {value:key for key, value in dict_old.items()}
print(dict_new)