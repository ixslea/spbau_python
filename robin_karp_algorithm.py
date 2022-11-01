#!/usr/bin/env python3

"""
Реализация алгоритма Рабина-Карпа с модульными тестами
"""

import unittest


def rabin_karp(text, pattern):
    """
    Поиск всех вхождений алгоритмом Рабина-Карпа
    Параметры:
    ----------
        text: str
            текст
        pattern: str
            образец
    Возвращаемое значение
    ---------------------
        список позиций в тексте, с которых начинаются вхождения образца
    """
    d = 256
    mod_num = 11
    text_len = len(text)
    pattern_len = len(pattern)
    h = pow(d, pattern_len - 1) % mod_num
    multiplier_pattern = 0
    multiplier_text = 0
    result = []
    if text_len == 0:
        return result

    if pattern_len == 0:
        return list(range(text_len))

    for i in range(pattern_len):
        multiplier_pattern = (d * multiplier_pattern + ord(pattern[i])) % mod_num
        multiplier_text = (d * multiplier_text + ord(text[i])) % mod_num

    for s in range(text_len - pattern_len + 1):
        if multiplier_pattern == multiplier_text:
            match = True
            for i in range(pattern_len):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]

        if s < text_len - pattern_len:
            multiplier_text = (multiplier_text - h * ord(text[s])) % mod_num
            multiplier_text = (multiplier_text * d + ord(text[s + pattern_len])) % mod_num
            multiplier_text = (multiplier_text + mod_num) % mod_num
    return result


class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Функция должна возвращать пустой список, если текст пустой, даже если образец пустой"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )

# Должно выдать:
# --------------
# Ran ... tests in ...s
# OK

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
