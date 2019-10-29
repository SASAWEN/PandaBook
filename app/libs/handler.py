"""
    Created by cala at 2019-10-25
"""

def is_isbn_or_key(word):
    # isbn格式：
    # isbn13 13个数字组成
    # isbn10 10个数字组成（含'-'）
    isbn_or_key = 'key'
    if len(word) == 13 or word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key

