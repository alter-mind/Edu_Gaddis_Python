SAUSAGE_PACK = 10
BUNS_PACK = 8
people = int(input('Enter number of people: '))
hot_dog_per_person = int(input('Enter number of hot dog per person: '))
hot_dogs = people * hot_dog_per_person
sausage_pack = hot_dogs // SAUSAGE_PACK + 1
print('min sausage pack:', sausage_pack)
buns_pack = hot_dogs // BUNS_PACK + 1
print('min buns pack:', buns_pack)
print('Sausages remain:', SAUSAGE_PACK * sausage_pack - hot_dogs)
print('Buns remain:', BUNS_PACK * buns_pack - hot_dogs)

