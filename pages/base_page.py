from playwright.sync_api import Page


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод открытия ссылок
        self.page.goto(url)

    def reload(self):  # Метод для перезагрузки страницы
        self.page.reload()
