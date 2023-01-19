start= b'r\xc3\xa9sum\xc3\xa9'
print(start)
second=start.decode()
print(second)
Thirh=second.encode('Latin1','ignore')
print(Thirh)
d=Thirh.decode('Latin1')
print(d)


