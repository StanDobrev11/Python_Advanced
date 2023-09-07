def find_all_indices(values, value):
    idx = 0
    indices = []
    while True:
        try:
            new_idx = values.index(value, idx)
            indices.append(new_idx)
            idx = new_idx + 1
        except ValueError:
            break

    return indices


print(find_all_indices([1, 2, 3, 4, 2, 1, 3, 1, 5], 1))

tt = (1, 2, 3)
a, *rest = tt
print(a, rest)