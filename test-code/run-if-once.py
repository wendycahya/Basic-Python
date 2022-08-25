a = 1
b = 2
c = False
e = 0

d = [1, 2, 3, 4]
index = 0
for x in d:
    e = a + x
    if b == 2 and not(c):
        print("running sekali saja")
        c = True
    index = index + 1
    print("Step index: ", index)