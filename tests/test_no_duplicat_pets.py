from conftest import *

def test_no_duplicate_pets(go_to_my_pets):
    #Поверка, что на странице со списком моих питомцев нет повторяющихся питомцев

    #Сохранение в переменную pet_data элементов с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    #Перебор данных из pet_data: оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    #Склейка имени, возраста и породы, получившиеся склеенные слова добавляем в строку
    # и между ними вставляем пробел
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    #Получение списока из строки line
    list_line = line.split(' ')

    #Превращение списока в множество
    set_list_line = set(list_line)

    #Нахождение количества элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    #Из количества элементов списка вычитается количество элементов множества
    result = a - b

    #Если количество элементов == 0, то карточки с одинаковыми данными отсутствуют
    assert result == 0