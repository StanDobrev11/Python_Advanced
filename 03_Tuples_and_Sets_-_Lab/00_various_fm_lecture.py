# def find_all_indices(values, value):
#     idx = 0
#     indices = []
#     while True:
#         try:
#             new_idx = values.index(value, idx)
#             indices.append(new_idx)
#             idx = new_idx + 1
#         except ValueError:
#             break
#
#     return indices
#
#
# print(find_all_indices([1, 2, 3, 4, 2, 1, 3, 1, 5], 1))
#
# tt = (1, 2, 3)
# a, *rest = tt
# print(a, rest)


class CustomSet:
    resize_factor = 0.7

    def __init__(self):
        self.count = 0
        self.capacity = 8
        self.values = [None] * self.capacity

    def execute_resize_check(self):
        return self.capacity * self.resize_factor <= self.count

    def resize(self):
        self.count = 0
        old_values = self.values
        self.capacity *= 2
        self.values = [None] * self.capacity
        for nested_lists in old_values:
            if nested_lists:
                for value in nested_lists:
                    self.add(value)

    def get_index(self, value):
        return abs(hash(value)) % self.capacity

    def add(self, value):
        index = self.get_index(value)
        if self.values[index] is None:
            self.values[index] = []
        if value not in self.values[index]:
            self.values[index].append(value)
            self.count += 1
        if self.execute_resize_check():
            self.resize()

    def remove(self, value):
        if not self.contains(value):
            return
        index = self.get_index(value)
        self.values[index].remove(value)
        self.count -= 1

    def contains(self, value):
        index = self.get_index(value)
        if not self.values[index]:
            return False
        if value not in self.values[index]:
            return False
        return True

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.count



ss = CustomSet()
# ss.add('abc')
#
values = ['a',
          1,
          0,
          -1,
          (2, 3, 4),
          3.14,
          'Pesho',
          'detail',
          'glass',
          'wood',
          54,
          'pepper',
          'door',
          'handle',
          None,
          'phone',
          'rocket',
          12234,
          'chess',
          -67.876,
          ]

for x in values:
    ss.add(x)

# print(ss.values)
# print(len(values))
# print(len(ss.values))
# count = 0
# for value in ss.values:
#     if value:
#         count += 1
# print(count)
# print(ss.contains('Pesho'))
# ss.remove('Pesho')
# print(ss.values)
# print(ss.contains('Pesho'))
# print(54 in ss)
# ss.remove(54)
# print(54 in ss)
print(54 in ss)
print(len(ss))
print(type(ss))
print(ss)