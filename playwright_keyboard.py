from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    # Открываем браузер и создаем новую страницу
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'user@gmail.com':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.press(character, delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press('ControlOrMeta+A')

    # Ждем 5 секунд для наглядности результата
    page.wait_for_timeout(5000)
