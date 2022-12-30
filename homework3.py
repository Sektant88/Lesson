SourceFile=open('pyton.txt','w')
f=input()
a=f[0:5]
b=f[6:]
c='%s,%s' %(b,a)
d='{},{}'.format(a,b)
e='!{0},{1}?'.format(a,b)
print(f,a,b,c,d.swapcase(),e, sep='<<<>>>', file=SourceFile)
