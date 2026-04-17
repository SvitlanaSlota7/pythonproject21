def count_words(file_obj):
    """Кількість слів у текстовому файлі."""
    content = file_obj.read()
    if not content:
        return 0
    words = content.split()
    return len(words)