# create an empty set
s = set()
# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)
s.add(3)
print(s)

s.remove(3)
print(s)
print(f"the set has {len(s)} elements.")