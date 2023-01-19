start= b'r\xc3\xa9sum\xc3\xa9'
print(start)
second=start.decode()
print(second)
Thirh=second.encode('Latin1')
print(Thirh)
d=Thirh.decode('utf-8','ignore')
print(d)


