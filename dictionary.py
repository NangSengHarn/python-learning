person={
    'name' : 'nang seng harn',
    'age' : 20
}
print(person['name']);

person['hair_color']='black';
print(person);

print('name' in person)
print('school' in person)

if 'name' in person :
    print(person['name']);

personKeys=list(person.keys());
print(personKeys);
personValues=list(person.values());
print(personValues);