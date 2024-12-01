my_dict = {'Zhenya': 1984, 'Denis': 1983, 'Nikita': 2009, 'Danya': 2015}
print(my_dict)
print(my_dict.get('Danya'))
print(my_dict.get('Sasha'))
my_dict.update({'Tanya': 1960, 'Lena': 1962})
print(my_dict)
x = my_dict.pop('Nikita')
print(x)
print(my_dict)

my_set = {1, 2, 2, 5, 0.5, 2.5, 4, 0.5, 'str'}
print(my_set)
my_set.add(5.4)
my_set.add('egg')
my_set.discard(0.5)
print(my_set)
