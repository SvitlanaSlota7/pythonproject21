import datetime
import os

class MyFileManager:
    # Лічильник для всієї програми
    execution_counter = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Збільшуємо лічильник
        MyFileManager.execution_counter += 1

        # Логування з часом
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Вхід у контекст: {self.filename}")
        print(f"Номер операції: {MyFileManager.execution_counter}")

        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Вихід з контексту: {self.filename}")

        if self.file:
            self.file.close()

        # Обробка винятків за документацією Python
        if exc_type is not None:
            print(f"Сталася помилка: {exc_val}")
            return False

        return True

folder_path = r"E:\PyCharm\pythonproject_21\task_1"
file_path = os.path.join(folder_path, "test_log.txt")

# Перевірка наявності папки
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

try:
    with MyFileManager(file_path, 'w') as f:
        f.write("Цей текст збережено у форматі UTF-8.\n")
        f.write("Українська мова відображатиметься коректно в будь-якому редакторі.")

        print("Текстові дані успішно записані у файл.")
except Exception as e:
    print(f"Критична помилка програми: {e}")