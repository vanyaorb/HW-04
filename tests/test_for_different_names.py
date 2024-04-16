from conftest import *

def test_all_pets_have_different_names(go_to_my_pets):
    #Поверка, что на странице со списком моих питомцев у всех питомцев разные имена

    #Сохранение в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    #Перебор данных из pet_data: оставляем имя, возраст, и породу остальное меняется на пустую строку
    # и разделяется по пробелу. Выбираем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    #Перебор имен, и если имя повторяется то прибавляем к счетчику r единицу.
    #Провтор, если r == 0 то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(f'\n {r}')
    print(f'\n {pets_name}')