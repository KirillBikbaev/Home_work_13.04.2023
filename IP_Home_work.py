ip = input('Введите IP-адрес: ')
ip_address = ip.split('.')
result = all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_address) # проверка на правильность всех частей IP-адреса с помощью all()
if result:
    print('Все числа со значением от 0 до 255')
else:
    any(not part.isdigit() or int(part) < 0 or int(part) > 255 for part in ip_address)
    print('Хотя бы одно число не со значением от 0 до 255')