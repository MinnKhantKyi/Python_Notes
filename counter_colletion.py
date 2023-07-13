from collections import Counter

a = Counter("gallad")
print(f"\n- [STRING IN COUNTER] {a}\n")

b = Counter(['a','a','b','c','c','a'])
print(f"\n- [LIST IN COUNTER] {b}\n")

c = Counter({'a':2, 'c':2, 'b':1})
print(f"\n- [DICTIONARY IN COUNTER] {c}")
print(f"\n- [most_commom METHOD] {c.most_common(2)}\n")

d = Counter(cats = 4, dogs = 7)
print(f"\n- [COUNTER] {d}")
print(f"\n- [ITEM IN COUNTER] d['cats'] {d['cats']}")
print(f"\n- [ITEM IN COUNTER] d['pets'] {d['pets']}\n")

c = Counter(a = 4, b = 2 , c = 0 , d = -2)
print(f"\n- [COUNTER] {c}")
d = ['a', 'b', 'b', 'c']
print(f"\n- [LIST] {d}")
c.subtract(d)
print(f"\n- [COUNTER.subtract(LIST)] {c}")

c.update(d)
print(f"\n- [COUNTER.update(LIST)] {c}\n")

d = Counter(['a', 'b', 'b', 'c'])
print(f"\n- [LIST] {d}")
print(f"\n- [COUNTER+LIST] {c+d}")
print(f"\n- [COUNTER-LIST] {c-d}\n")

print(f"\n- [INTERSECT] {c&d}\n")
print(f"\n- [MAXIMUM] {c|d}\n")