import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Variable
url = "http://barru.pythonanywhere.com/daftar"


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

     # Test Case Open Page Register
    def test_a_open_page_register(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)

        response_data = driver.find_element(By.CSS_SELECTOR, "#container > div.overlay-container > div > div.overlay-panel.overlay-left > h1").text
        self.assertIn(response_data, "Welcome Back!")

    # Test Case Login Positive
    def test_b_success_login(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("saf@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("saf123")
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertEqual(response_data, "Welcome")
        self.assertEqual(response_message, "Anda Berhasil Login")

    # Test Case Login Negative
    def test_c_failed_login_with_wrong_password(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("saf@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("test123")
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # Validasi Response
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, "Email atau Password Anda Salah")

    # Test Case Login Negative
    def test_d_failed_login_with_wrong_email(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("test@gmail.com")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("test123")
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        # Validasi Response
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, "Email atau Password Anda Salah")

    # Test Case Login Negative
    def test_e_failed_login_with_empty_email_and_password(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertEqual(response_data, "Email tidak valid")
        self.assertEqual(response_message, "Cek kembali email anda")

#     # Test Case Login Negative
#     def test_f_failed_login_with_wrong_email_format(self):

#         driver = self.driver
#         driver.get(url)
#         time.sleep(3)
#         driver.find_element(By.ID, "email").send_keys("saf")
#         time.sleep(1)

#         email_error = driver.find_element(By.ID,"email").get_attribute("validationMessage")
#         print("PRINT ERROR")
#         print(email_error)

#         driver.find_element(By.ID, "password").send_keys("saf123")
#         time.sleep(1)
#         driver.find_element(By.ID, "signin_login").click()
#         time.sleep(1)

#         self.assertIn(email_error, "Please Include")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
