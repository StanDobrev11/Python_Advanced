def cookbook(*args):  # args (name, cuisine, [ingredient1, ingredient2....ingredientN])

    cuisine_book = {}

    for recipy in args:
        name, cuisine, ingredients = recipy

        if cuisine not in cuisine_book:
            cuisine_book[cuisine] = {}

        if name not in cuisine_book[cuisine]:
            cuisine_book[cuisine][name] = ingredients

    result = []
    for cuisine, recipies in sorted(cuisine_book.items(), key=lambda item: (-len(item[1]), item[0])):
        result.append(f"{cuisine} cuisine contains {len(recipies)} recipes:")
        for recipy, ingredients in sorted(recipies.items()):
            result.append(f"  * {recipy} -> Ingredients: {', '.join(ingredients)}")

    return '\n'.join(result)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
