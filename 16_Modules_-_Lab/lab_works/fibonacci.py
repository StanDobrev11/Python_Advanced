def create_sequence(count):
    nums = []
    if count == 1:
        nums.append(0)
    if count == 2:
        nums.extend([0, 1])

    else:
        nums = [0, 1]
        for _ in range(2, count):
            next_num = nums[-1] + nums[-2]
            nums.append(next_num)

    return nums


def locate(number, seq):
    try:
        index = seq.index(number)
        return f"The number - {number} is at index {index}"
    except ValueError:
        return f"The number {number} is not in the sequence"
