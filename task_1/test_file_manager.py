import unittest
import os
from file_manager import MyFileManager


class TestMyFileManager(unittest.TestCase):
    def setUp(self):
        """Виконується перед кожним тестом"""
        self.filename = "test_case.txt"
        self.content = "Тестовий контент"

    def tearDown(self):
        """Виконується після кожного тесту. Видаляємо сміття."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_file_writing_positive(self):
        """Перевірка успішного запису у файл."""
        with MyFileManager(self.filename, 'w') as f:
            f.write(self.content)

        # Перевіряємо, чи файл існує і чи дані збігаються
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), self.content)

    def test_counter_increments(self):
        """Перевірка, чи працює лічильник """
        initial_count = MyFileManager.execution_counter
        with MyFileManager(self.filename, 'w') as _:
            pass
        self.assertEqual(MyFileManager.execution_counter, initial_count + 1)

    def test_file_not_found_error(self):
        # Спроба відкрити неіснуючий файл ('r') має викликати FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            with MyFileManager("non_existent.txt", 'r') as f:
                f.read()

    def test_runtime_error_inside_context(self):
        """Перевірка закриття файлу, якщо всередині 'with' сталася помилка."""
        try:
            with MyFileManager(self.filename, 'w') as f:
                f.write("Дані")
                raise ValueError("Раптова помилка під час виконання")
        except ValueError:
            pass
        # Перевіряємо, чи файл був закритий. Спроба його видалити не має викликати PermissionError

        try:
            os.remove(self.filename)
        except PermissionError:
            self.fail("Файл залишився відкритим після помилки всередині контексту")

    def test_invalid_mode_error(self):
        """Перевірка передачі числа замість рядка"""
        with self.assertRaises(TypeError):
            with MyFileManager(self.filename, 123) as f:
                f.write("тест")


if __name__ == '__main__':
    unittest.main()