"""
Write a function called accommodate_new_pets that receives information about the available capacity of the
hotel, the maximum weight allowed per pet, the pet types, and their weight, and returns the result after the
accommodation. The function will receive a different number of arguments. The arguments will be passed as
follows:
 The first argument will be the available capacity of your hotel ‐ an integer in the range [0, 50];
 The second argument will be the maximum weight limit ‐ a float number representing the pet’s maximum
allowed weight;
 The following arguments will be the tuples with two elements ‐ the first one is the pet type (string), and the
second one is the pet weight (float);
After receiving the information and calling the function, the program should start tracking the accommodation
process:
 Take the pet type from each tuple successively and if you have enough capacity, accommodate it, and
proceed to the next one. Keep in mind that you will also need to track the total number of pets for each pet
type you accommodate.
 If a pet’s weight exceeds the maximum weight limit, ignore it, and proceed to the next one.
 If the available capacity is 0 (zero), STOP accommodating!
o You are not supposed to check the weight of the unaccommodated pets (if any) when you run out of
space.
In the end:
 If you’ve managed to accommodate all pets, return the message: "All pets are accommodated!
Available capacity: {available_capacity}."
 Otherwise, return the message: "You did not manage to accommodate all pets!"
 On the following lines return the accommodated pet types and number of pets, ordered ascending
(alphabetically) by pet type. Each on a new line:
"Accommodated pets:
{pet_type1}: {number}
{pet_type2}: {number}
…
{pet_typeN}: {number}"

print(accommodate_new_pets(
10,
15.0,
("cat", 5.8),
("dog", 10.0),
))
                All pets are accommodated! Available capacity: 8.
                Accommodated pets:
                cat: 1
                dog: 1
print(accommodate_new_pets(
10,
10.0,
("cat", 5.8),
("dog", 10.5),
("parrot", 0.8),
("cat", 3.1),
))
                All pets are accommodated! Available capacity: 7.
                Accommodated pets:
                cat: 2
                parrot: 1
print(accommodate_new_pets(
2,
15.0,
("dog", 10.0),
("cat", 5.8),
("cat", 2.7),
))
                You did not manage to accommodate all pets!
                Accommodated pets:
                cat: 1
                dog: 1
"""
from collections import deque


def accommodate_new_pets(capacity, max_weight, *args):
    pet_list = deque(args)
    accommodated = {}
    while pet_list:
        if capacity > 0:
            animal = pet_list.popleft()
            name, weight = animal
            if weight > max_weight:
                continue
            else:
                capacity -= 1
                if name not in accommodated:
                    accommodated[name] = 0
                accommodated[name] += 1
        else:
            break


    if pet_list:
        output = f"You did not manage to accommodate all pets!\n"
    else:
        output = f"All pets are accommodated! Available capacity: {capacity}.\n"

    output += ("Accommodated pets:\n" +
               '\n'.join([f"{key}: {value}" for key, value in sorted(accommodated.items())]))

    return output


print(accommodate_new_pets(
    1,
    3,
    ("dog", 10.1)
    ,
    ("cat", 5.8),
    ("cat", 2.7),
))

# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))

# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))

# print(accommodate_new_pets(
# 2,
# 15.0,
# ("dog", 10.0),
# ("cat", 5.8),
# ("cat", 2.7),
# ))

# from collections import deque
#
#
# def accommodate_new_pets(capacity: int, weight_limit: float, *args):
#     accommodated_pets = {}
#     args = deque(args)
#     while capacity > 0:
#
#         try:
#             next_pet = args.popleft()
#         except IndexError:
#             break
#
#         pet_type, pet_weight = next_pet
#
#         if pet_weight > weight_limit:
#             continue
#
#         if pet_type not in accommodated_pets:
#             accommodated_pets[pet_type] = []
#
#         accommodated_pets[pet_type].append(pet_weight)
#         capacity -= 1
#
#     if not args:
#         text = [f"All pets are accommodated! Available capacity: {capacity}."]
#
#     else:
#         text = ["You did not manage to accommodate all pets!"]
#
#     text += ['Accommodated pets:']
#     text += [f"{key}: {len(value)}" for key, value in sorted(accommodated_pets.items())]
#
#     return '\n'.join(text)