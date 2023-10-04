"""
Write a function called forecast that stores information about the weather, and returns sorted information for
all locations. The function will receive a different number of arguments. The arguments will be passed as tuples
with two elements ‐ the first one is the location, and the second one is the weather:
 Location name: string
o any string
 Weather: string
o "Sunny"
o "Rainy"
o "Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations
with cloudy weather, and last are the locations with rainy weather. For each sequence of locations (e.g. all sunny
locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
 There will be no input from the console, just parameters passed to your function
Output
 The output should look like this:
"{first_sorted_location} ‐ {weather}"
"{second_sorted_location} ‐ {weather}"
…
"{last_sorted_location} ‐ {weather}"
Constraints
 Each tuple given will always contain the location with its weather.
 You will never receive the same location twice or more times.
print(forecast(
("Sofia", "Sunny"),
("London", "Cloudy"),
("New York", "Sunny")))
                            New York ‐ Sunny
                            Sofia ‐ Sunny
                            London ‐ Cloudy
print(forecast(
("Beijing", "Sunny"),
("Hong Kong", "Rainy"),
("Tokyo", "Sunny"),
("Sofia", "Cloudy"),
("Peru", "Sunny"),
("Florence", "Cloudy"),
("Bourgas", "Sunny")))
                            Beijing ‐ Sunny
                            Bourgas ‐ Sunny
                            Peru ‐ Sunny
                            Tokyo ‐ Sunny
                            Florence ‐ Cloudy
                            Sofia ‐ Cloudy
                            Hong Kong ‐ Rainy
print(forecast(
("Tokyo", "Rainy"),
("Sofia", "Rainy")))
                            Sofia ‐ Rainy
                            Tokyo ‐ Rainy
"""


def forecast(*args):
    weather = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }
    for location, frcst in args:
        weather[frcst].append(location)

    result = []
    for key, values in weather.items():
        for value in sorted(values):
            result.append(f"{value} - {key}")

    return '\n'.join(result)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
