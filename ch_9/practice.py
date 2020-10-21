numbers = [1, 2, 3, 4, 4, 4, 2, 1, 1, 1, 1, 2, 2, 2, 5]
number_dictionary = {}
for i in numbers:
    if i not in number_dictionary:
        number_dictionary[i] = numbers.count(i)
        print(number_dictionary.get(i))
print(number_dictionary)

for i in numbers:
    if i in number_dictionary.keys():
        del number_dictionary[i]

print(number_dictionary)

number_dictionary[0] = numbers
for num_list in number_dictionary.values():
    for num in num_list:
        print(num, end=' ')

number_dictionary.clear()
print()
print(number_dictionary)

words = {'abra': 'cadabra', 'boo': 'hoo'}
print(words.get('abra'))
print(words.pop('boo'))
print(words)

my_set = set('hello')
print(type(my_set))
num_set = set(numbers)
print(num_set)
num_set.add(1)
num_set.add(6)
print(num_set)
num_set.update([8, 332, 90])
print(num_set)
num_set.remove(332)
print(num_set)
for i in num_set:
    print(i)
