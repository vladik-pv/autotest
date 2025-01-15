import pytest
from string_utils import StringUtils


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python program", "Python program"),
    ("1st place", "1st place"),
    ("", ""),
    (" a new beginning", " a new beginning")
])
def test_capitilize(input_str, expected):
    utils = StringUtils()
    assert utils.capitilize(input_str) == expected


class TestStringTrim:
    @pytest.mark.parametrize("input_str, expected_result", [
        ("   skypro", "skypro"),
        ("   hello world", "hello world"),
        ("      python programming", "python programming"),
        ("singleWord", "singleWord"),
        ("", ""),
        ("   leading spaces", "leading spaces")
    ])
    def test_trim(self, input_str, expected_result):
        utils = StringUtils()
        assert utils.trim(input_str) == expected_result


class TestStringUtils:
    @pytest.mark.parametrize("input_str, delimiter, expected_result", [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("", None, []),
        ("   ", None, []),
        ("apple|banana|cherry", "|", ["apple", "banana", "cherry"]),
        ("one", None, ["one"])
    ])
    def test_to_list(self, input_str, delimiter, expected_result):
        utils = StringUtils()
        assert utils.to_list(input_str, delimiter) == expected_result


class TestStringContains:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("Hello World", "H", True),
        ("12345", "3", True),
        ("abcdefg", "e", True),
        ("SkyPro", "U", False),
        ("Hello World", "x", False),
        ("12345", "6", False),
        ("abcdefg", "z", False),
        ("", "a", False),    # Пустая строка
        ("a", "", True),    # Искомый символ пустой
        ("", "", True),      # Оба пустые
        ("New String", "N", True),  # Новый случай
        ("Another Test", "T", True)  # Ещё один новый случай
    ])
    def test_contains(self, string_utils, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected


class TestStringSymbol:
    @pytest.fixture
    def string_processor(self):
        return StringUtils()

    @pytest.mark.parametrize(
        "input_str, symbol, expected_result", [
            ("SkyPro", "k", "SyPro"),
            ("SkyPro", "Pro", "Sky"),
            ("Hello World", "o", "Hell Wrld"),
            ("TestString", "a", "TestString"),
            ("", "x", "")
        ]
    )
    def test_delete_symbol(
        self, string_processor, input_str, symbol, expected_result
    ):
        assert string_processor.delete_symbol(
            input_str, symbol
            ) == expected_result


class TestStringWith:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    @pytest.mark.parametrize(
        "input_str, prefix, expected", [
            ("SkyPro", "S", True),
            ("SkyPro", "P", False),
            ("Hello World", "H", True),
            ("", "A", False),
            ("Python", "", True),
            ("   Leading spaces", " ", True),
            ("MixedCase", "m", False),
            ("123456", "1", True)
        ]
    )
    def test_starts_with(self, string_utils, input_str, prefix, expected):
        assert string_utils.starts_with(input_str, prefix) == expected


class TestEndWith:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    @pytest.mark.parametrize(
        "input_str, suffix, expected", [
            ("SkyPro", "o", True),
            ("SkyPro", "y", False),
            ("Hello World", "d", True),
            ("", "A", False),
            ("Python", "", True),
            ("   Trailing spaces", " ", True),
            ("MixedCase", "e", True),
            ("123456", "6", True)
        ]
    )
    def test_end_with(self, string_utils, input_str, suffix, expected):
        assert string_utils.end_with(input_str, suffix) == expected


class TestIsEmpty:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    @pytest.mark.parametrize(
        "input_str, expected", [
            ("", True),
            (" ", True),
            ("   ", True),
            ("SkyPro", False),
            ("   SkyPro   ", False)
        ]
    )
    def test_is_empty(self, string_utils, input_str, expected):
        assert string_utils.is_empty(input_str) == expected


class TestToString:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    @pytest.mark.parametrize(
        "input_list, separator, expected", [
            ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
            (["Sky", "Pro"], ", ", "Sky, Pro"),
            (["Sky", "Pro"], "-", "Sky-Pro"),
            ([], ", ", ""),
            ([1], ", ", "1"),
            ([1, 2], ", ", "1, 2"),
        ]
    )
    def test_list_to_string(
        self, string_utils, input_list, separator, expected
    ):
        assert string_utils.list_to_string(input_list, separator) == expected
