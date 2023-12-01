data = [
    ('Austin', 28, 25875246),
    ('Boston', 24, 30568456),
    ('Chicago', 32, 11548625),
    ('Denver', 29, 12546215),
    ('Los Angeles', 35, 32548321),
    ('Miami', 22, 16254842),
    ('New York', 31, 21548328),
    ('Phoenix', 27, 11549842),
    ('San Francisco', 30, 15264476),
    ('Seattle', 26, 21548624)
]

l = []
for i in data:
    pop_nums = i[2]
    l.append(pop_nums)

avg = sum(l) / len(l)
print(avg)
