import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_is_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Небольшая пауза, чтобы визуально проверить смену языка (опционально)
    time.sleep(5)
    
    # Ищем кнопку добавления в корзину по CSS-селектору
    # Класс .btn-add-to-basket есть на этой странице
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверяем, что кнопка существует (find_element выбросит исключение, если её нет)
    assert button is not None, "Кнопка добавления в корзину не найдена"
    
    # Дополнительная проверка: текст кнопки не пустой
    assert button.text != "", "Текст на кнопке пустой"
    
    # Для отладки можно вывести текст кнопки в консоль
    print(f"\nButton text: {button.text}")
