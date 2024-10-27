import unittest
from unittest.mock import patch
from io import BytesIO

from src.fetch_selector import fetch_selector

test_url = "https://example.com"


class TestAddFunction(unittest.TestCase):
    @patch("src.fetch_selector.urlopen")
    def test_fetch_selector(self, mock_urlopen):
        """href要素を取得できること"""

        mock_urlopen.return_value = BytesIO(
            b"""
            <a class='test' href='href_value'>text</a>
            """
        )
        bs_elements = fetch_selector(url=test_url, selector=".test")
        result = str(bs_elements[0])
        expected = '<a class="test" href="href_value">text</a>'

        self.assertEqual(result, expected)

    @patch("src.fetch_selector.urlopen")
    def test_fetch_selectors(self, mock_urlopen):
        """複数のhref要素を取得できること"""

        mock_urlopen.return_value = BytesIO(
            b"""
            <div>
                <a class='test' href='href_value'>text</a>
                <a class='test' href='href_value'>text</a>
                <a class='test' href='href_value'>text</a>
            </div>
            """
        )
        bs_elements = fetch_selector(url=test_url, selector=".test")
        result = [str(bs_element) for bs_element in bs_elements]
        expected = [
            '<a class="test" href="href_value">text</a>',
            '<a class="test" href="href_value">text</a>',
            '<a class="test" href="href_value">text</a>',
        ]

        self.assertEqual(result, expected)

    @patch("src.fetch_selector.urlopen")
    def test_fetch_not_exit_selector(self, mock_urlopen):
        """aタグがない場合は空リストを返すこと"""

        mock_urlopen.return_value = BytesIO(
            b"""
            <div></div>
            """
        )
        result = fetch_selector(url=test_url, selector=".test")
        expected = []

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
