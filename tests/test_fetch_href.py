import unittest
from unittest.mock import patch
from io import BytesIO

from src.fetch_href import fetch_href

test_url = "https://example.com"


class TestAddFunction(unittest.TestCase):
    @patch("src.fetch_href.urlopen")
    def test_fetch_href(self, mock_urlopen):
        """href要素を取得できること"""

        mock_urlopen.return_value = BytesIO(
            b"""
            <a class='test' href='href_value'>text</a>
            """
        )
        result = fetch_href(url=test_url, href_class="test")
        expected = [{"text": "text", "href": "href_value"}]

        self.assertEqual(result, expected)

    @patch("src.fetch_href.urlopen")
    def test_fetch_href_a_lot(self, mock_urlopen):
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
        result = fetch_href(url=test_url, href_class="test")
        expected = [
            {"text": "text", "href": "href_value"},
            {"text": "text", "href": "href_value"},
            {"text": "text", "href": "href_value"},
        ]

        self.assertEqual(result, expected)

    @patch("src.fetch_href.urlopen")
    def test_fetch_href_a_lot(self, mock_urlopen):
        """aタグがない場合は空リストを返すこと"""

        mock_urlopen.return_value = BytesIO(
            b"""
            <div></div>
            """
        )
        result = fetch_href(url=test_url, href_class="test")
        expected = []

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
