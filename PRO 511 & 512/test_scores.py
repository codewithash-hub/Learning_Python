test_scores = { 'Kayla' : [88, 92, 100], 
               'Luis' : [95, 74, 81], 
               'Sophie' : [72, 88, 91], 
               'Ethan' : [70, 75, 78] }

for k, v in test_scores.items():
    avg = sum(v) / len(v)
    
    print()
    print(k, v)
    print(f'{k}\t {avg: .2f}')
    