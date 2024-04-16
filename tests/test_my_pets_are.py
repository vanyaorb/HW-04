from conftest import *

def test_all_pets_are_present(go_to_my_pets):
    #Проверка, что на странице со списком моих питомцев присутствуют питомцы

    #Сохранение в переменную statistic элементов статистики
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    #Сохранение в переменную pets элементов карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    #Получение количества питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    #Получение количества карточек питомцев
    number_of_pets = len(pets)

    #Проверка, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets