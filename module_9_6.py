def all_variants(text):
    a = len(text)
    sub = []
    for start in range(a):
        for end in range(start + 1, a + 1):
            sub.append(text[start:end])

    sub.sort(key=lambda x: (len(x), x))

    for subs in sub:
        yield subs



text = 'abc'
gener = all_variants((text))
for var in gener:
    print(var)