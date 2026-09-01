from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    # Открываем браузер и создаем новую страницу
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу авторизации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # Проверяем, что кнопка Login неактивна
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()
