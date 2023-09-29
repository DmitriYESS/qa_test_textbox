from .page.base_page import WorkPage

link = "https://demoqa.com/text-box"


def test_main_page(browser):
    page = WorkPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    name, email, current_address, permanent_address = page.fill_form() # получаем имя, почту, адреса
    page.submit_form() #жмем кнопку подтверждения
    r_name, r_email, r_c_address, r_p_address, result_text = page.get_result_text() #получаем выходные данные
    #ожидаемые данные
    exp_n = f'Name:{name}'
    exp_e = f'Email:{email}'
    exp_ca = f'Current Address :{current_address}'
    exp_pa = f'Permananet Address :{permanent_address}'

    #Сравнение данных
    if exp_n == r_name:
        print("name совпадет")
    else:
        print("name не совпадет")

    if exp_e == r_email:
        print("email совпадет")
    else:
        print("email не совпадет")

    if exp_ca == r_c_address:
        print("current_address совпадет")
    else:
        print("current_address не совпадет")

    if exp_pa == r_p_address:
        print("permanent_address совпадет")
    else:
        print("permanent_address не совпадет")
    # ожидаемый вывод текста полностью 2 вариант, тест будет падать если что-то не совпадает
    expected_result = f'Name:{name}\nEmail:{email}\nCurrent Address :{current_address}\nPermananet Address :{permanent_address}'

    assert result_text == expected_result, print("Данные не совпадают")

    # команды запуска: pytest --browser_name=firefox test_main_page.py, pytest --browser_name=chrome test_main_page.py
    # pytest test_main_page.py запустит Chrome по умолчанию
