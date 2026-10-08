from my_set import MySet

set_of_str = MySet()

print(set_of_str.add('one'))
print(set_of_str.add('two'))
print(set_of_str.add('one'))

print('one' in set_of_str)
print('three' in set_of_str)

print(len(set_of_str))

for element in set_of_str:
    print(element)