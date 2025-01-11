import pytest
from string_utils import StringUtils


def test_capitilize():
    utils = StringUtils()

    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("python program") == "Python program"
    assert utils.capitilize("1st place") == "1st place"
    assert utils.capitilize("") == ""
    assert utils.capitilize(" a new beginning") == " a new beginning"


def test_trim():
    utils = StringUtils()

    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("   hello world") == "hello world"
    assert utils.trim("      python programming") == "python programming"
    assert utils.trim("singleWord") == "singleWord"
    assert utils.trim("") == ""
    assert utils.trim("   leading spaces") == "leading spaces"


def test_to_list():
    utils = StringUtils()

    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert utils.to_list("") == []
    assert utils.to_list("   ") == []
    assert utils.to_list("apple|banana|cherry", "|") == [
        "apple", "banana", "cherry"
        ]
    assert utils.to_list("one") == ["one"]


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

    def test_delete_symbol(self, string_processor):
        assert string_processor.delete_symbol
        ("SkyPro", "k") == "SyPro"
        assert string_processor.delete_symbol(
            "SkyPro", "Pro"
            ) == "Sky"
        assert string_processor.delete_symbol(
            "Hello World", "o"
            ) == "Hell Wrld"
        assert string_processor.delete_symbol(
            "TestString", "a"
            ) == "TestString"
        assert string_processor.delete_symbol("", "x") == ""


class TestStringWith:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    def test_starts_with(self, string_utils):
        assert string_utils.starts_with("SkyPro", "S")
        assert not string_utils.starts_with("SkyPro", "P")
        assert string_utils.starts_with("Hello World", "H")
        assert not string_utils.starts_with("", "A")
        assert string_utils.starts_with("Python", "")
        assert string_utils.starts_with("   Leading spaces", " ")
        assert not string_utils.starts_with("MixedCase", "m")
        assert string_utils.starts_with("123456", "1")


class TestEndWith:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    def test_end_with(self, string_utils):
        assert string_utils.end_with("SkyPro", "o")
        assert not string_utils.end_with("SkyPro", "y")
        assert string_utils.end_with("Hello World", "d")
        assert not string_utils.end_with("", "A")
        assert string_utils.end_with("Python", "")
        assert string_utils.end_with("   Trailing spaces", " ")
        assert string_utils.end_with("MixedCase", "e")
        assert string_utils.end_with("123456", "6")


class TestIs_empty:
    @pytest.fixture
    def string_utils(self):
        return StringUtils()

    def test_is_empty(self, string_utils):
        assert string_utils.is_empty("")
        assert string_utils.is_empty(" ")
        assert string_utils.is_empty("   ")
        assert not string_utils.is_empty("SkyPro")
        assert not string_utils.is_empty("   SkyPro   ")


class Test_to_string:
    @pytest.fixture
    def list_utils(self):
        return StringUtils()

    def test_list_to_string(self, string_utils):
        assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert string_utils.list_to_string([]) == ""
        assert string_utils.list_to_string([1]) == "1"
        assert string_utils.list_to_string([1, 2]) == "1, 2"
