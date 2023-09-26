# nums = [int(x) for x in input().split(', ')]
#
# print(nums)
def check_fireworks(fireworks):
    return [False if value >= 3 else True for value in fireworks.values()]

fireworks = {
    'Palm': 3,
    'Willow': 3,
    'Crossette': 3,
}
print(check_fireworks(fireworks))
print(not any(check_fireworks(fireworks)))