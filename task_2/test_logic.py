import pytest
import os
from file_manager import FileManager
from logic import count_words


@pytest.fixture
def temp_file():

    file_path = "test_temp.txt"
    with FileManager(file_path, "w") as f:
        f.write("Python is amazing and powerful")

    with FileManager(file_path, "r") as f:
        yield f  # Передаємо об'єкт файлу в тест

    # Код після yield виконується після завершення тесту
    if os.path.exists(file_path):
        os.remove(file_path)

def test_count_words_logic(temp_file):

    result = count_words(temp_file)
    assert result == 5  # "Python", "is", "amazing", "and", "powerful"