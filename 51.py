def same_by(func, collection):
    return len(list(filter(func, collection))) == 0

values = [0, 2, 10, 6, 8, 12, 24, 1]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')    