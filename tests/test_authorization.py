import pytest

from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    'email, password',
    [
        pytest.param('user.name@gmail.com', 'password', id='Invalid email and password'),
        pytest.param('user.name@gmail.com', '  ', id='Invalid email and empty password (with two spaces)'),
        pytest.param('  ', 'password', id='Empty email (with twp spaces) and invalid password'),
    ]
)
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user@gmail.com')

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('password')

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
