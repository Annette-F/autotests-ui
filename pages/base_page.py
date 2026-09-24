from typing import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод открытия ссылок
        self.page.goto(url)

    def reload(self):  # Метод для перезагрузки страницы
        self.page.reload()

    def check_current_url(self, expected_url:Pattern[str]):
        expect(self.page).to_have_url(expected_url)
