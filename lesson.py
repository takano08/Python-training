r = [1,2,3,4,5,1,2,3]
print(r.index(3,3))

print(r.count(3))
if 5 in r:
    print('exist')

if 100 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)