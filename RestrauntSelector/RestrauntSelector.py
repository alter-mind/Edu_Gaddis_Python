def answer(answer):
    if answer == 'yes' or answer == '1' or answer == 'Yes' or answer == 'YES' or answer == 'да' or answer == 'Да' or answer == 'ДА':
        return True
    else:
        return False
joe = 'Gourmet Joe Burgers\n'
pizza = 'Central pizza\n'
cafe = 'Cafe around the corner\n'
mom = 'Dishes from italian mom\n'
chef = "Chef's kitchen"
vegetarian = answer(input('Will be a vegetarian on dinner?\n'))
vegan = answer(input('Will be a vegan on dinner?\n'))
dumm = answer(input('Will be a supporter of a gluten-free diet at dinner?\n'))
if vegetarian:
    if vegan:
        print(cafe + chef)
    elif dumm and not vegan:
        print(pizza + cafe + chef)
    else:
        print(pizza + mom + cafe + chef)
elif vegan:
    print(cafe + chef)
elif dumm:
    (pizza + cafe + chef)
else:
    print(joe + pizza + mom + cafe + chef)