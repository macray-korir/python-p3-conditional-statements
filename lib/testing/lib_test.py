from control_flow import admin_login, hows_the_weather, fizzbuzz, calculator
import io
import sys

class TestAdminLogin:
    def test_returns_access_granted_admin12345(self):
        assert admin_login("admin", "12345") == "Access granted"

    def test_returns_access_granted_ADMIN12345(self):
        assert admin_login("ADMIN", "12345") == "Access granted"

    def test_returns_access_denied_not_admin12345(self):
        assert admin_login("sudo", "12345") == "Access denied"
        assert admin_login("admin", "sudo") == "Access denied"
        assert admin_login("sudo", "pls") == "Access denied"

class TestHowsTheWeather:
    def test_under_40_brisk(self):
        assert hows_the_weather(33) == "It's brisk out there!"

    def test_under_65_chilly(self):
        assert hows_the_weather(55) == "It's a little chilly out there!"

    def test_above_85_too_dang_hot(self):
        assert hows_the_weather(99) == "It's too dang hot out there!"

    def test_65_to_85_perfect(self):
        assert hows_the_weather(75) == "It's perfect out there!"

class TestFizzBuzz:
    def test_returns_fizzbuzz_multiple_3_and_5(self):
        assert fizzbuzz(0) == "FizzBuzz"
        assert fizzbuzz(15) == "FizzBuzz"
        assert fizzbuzz(45) == "FizzBuzz"
    
    def test_returns_fizz_multiple_3_not_5(self):
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(33) == "Fizz"
        assert fizzbuzz(42) == "Fizz"
    
    def test_returns_buzz_multiple_5_not_3(self):
        assert fizzbuzz(5) == "Buzz"
        assert fizzbuzz(10) == "Buzz"
        assert fizzbuzz(50) == "Buzz"

    def test_returns_num_multiple_not_3_or_5(self):
        assert fizzbuzz(2) == 2
        assert fizzbuzz(13) == 13
        assert fizzbuzz(59) == 59

class TestCalculator:
    def test_returns_sum_if_plus(self):
        assert calculator("+", 1, 2) == 3
        assert calculator("+", 5, 7) == 12
        assert calculator("+", 9, 90) == 99

    def test_returns_difference_if_minus(self):
        assert calculator("-", 1, 2) == -1
        assert calculator("-", 7, 5) == 2
        assert calculator("-", 9, 9) == 0

    def test_returns_product_if_times(self):
        assert calculator("*", 1, 2) == 2
        assert calculator("*", 5, 7) == 35
        assert calculator("*", 9, 10) == 90

    def test_returns_quotient_if_divided_by(self):
        assert calculator("/", 1, 1) == 1
        assert calculator("/", 14, 7) == 2
        assert calculator("/", 90, 9) == 10

    def test_prints_invalid_returns_none_if_invalid(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        assert calculator('a', 1, 2) == "Invalid operation!"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Invalid operation!\n"

    def test_prints_invalid_returns_none_if_invalid(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        assert calculator('a', 1, 2) == "Invalid operation!"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Invalid operation!\n"