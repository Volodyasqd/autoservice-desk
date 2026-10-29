import unittest
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class TestAutoServiceUI(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://the-internet.herokuapp.com/login"
        self.auth_url = "https://the-internet.herokuapp.com/authenticate"

    def test_01_page_title_and_header(self):
        """Тест 1: Перевірка відкриття сторінки та наявності заголовка"""
        req = urllib.request.Request(self.base_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
            header = soup.find('h2')
            self.assertIsNotNone(header)
            self.assertIn("Login Page", header.text)
            print("\n[OK] Тест 1 пройдено: Сторінку успішно відкрито, заголовок перевірено.")

    def test_02_failed_login_validation(self):
        """Тест 2: Перевірка повідомлення про помилку при некоректних даних"""
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        data = urllib.parse.urlencode({'username': 'invalid_user', 'password': 'wrong_password'}).encode()
        req = urllib.request.Request(self.auth_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
        response = opener.open(req)
        soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
        flash_div = soup.find(id='flash')
        self.assertIsNotNone(flash_div)
        self.assertIn("Your username is invalid!", flash_div.text)
        print("[OK] Тест 2 пройдено: Повідомлення про некоректний вхід валідовано.")

    def test_03_successful_interaction(self):
        """Тест 3: Перевірка успішної взаємодії та отримання стану доступу"""
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        data = urllib.parse.urlencode({'username': 'tomsmith', 'password': 'SuperSecretPassword!'}).encode()
        req = urllib.request.Request(self.auth_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
        response = opener.open(req)
        soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
        flash_div = soup.find(id='flash')
        self.assertIsNotNone(flash_div)
        self.assertIn("You logged into a secure area!", flash_div.text)
        print("[OK] Тест 3 пройдено: Успішна авторизація та доступ підтверджено.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
