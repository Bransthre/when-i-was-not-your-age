import random as R

while True:
    x, y, z = (R.randint(1, 10) for i in range(3))
    aug_matrix = [[] for i in range(3)]
    for i in range(3):
        coeff_row = [R.randint(1, 10) for i in range(3)]
        scalar = sum([p[0] * p[1] for p in zip(coeff_row, [x, y, z])])
        aug_matrix[i] = coeff_row + [scalar]
    print('Augmented Matrix\n')
    for row in aug_matrix: print(row)
    print("\n")
    confirm = str(input("key enter to see results"))
    print(x, y, z)
    print("\n")