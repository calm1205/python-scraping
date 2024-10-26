import unittest

from src.page_increment import page_increment


class TestAddFunction(unittest.TestCase):
    def test_increment_pages(self):
        """pageがある場合はインクリメントされること"""

        test_url = "https://example.com?page=1"
        expected = "https://example.com?page=2"
        self.assertEqual(page_increment(url=test_url), expected)

    def test_not_exist_page(self):
        """pageがない場合は空文字列が返却されること"""

        test_url = "https://example.com"
        expected = ""
        self.assertEqual(page_increment(url=test_url), expected)


if __name__ == "__main__":
    unittest.main()
