from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    # Открываем браузер и создаем новую страницу
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    # # Пытаемся проверить, что несуществующий локатор виден на странице
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Пытаемся ввести текст в кнопку Login
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Пытаемся изменить текст заголовка
    page.evaluate(
        '''
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        '''
    )
