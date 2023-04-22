ip = input('Введите IP-адрес: ')
ip_address = ip.split('.')
if len(ip_address) != 4:
    print('Error')
else:
    result = all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_address) # проверка на правильность всех частей IP-адреса с помощью all()
    if result:
        print('Все числа со значением от 0 до 255')
    else:
        print('Хотя бы одно число не со значением от 0 до 255')