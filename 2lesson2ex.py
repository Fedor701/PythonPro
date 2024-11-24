import random
a = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю,./?!@#$%^&*()_1234567890"№;%:?='
b = int(input("Введите количество желаемых символов, для вашего пароля:"))
s = ''
for i in range(b):
    s += random.choice(a)
print(s)
