import unittest

from src.csv_format import get_csv_row


class TestAddFunction(unittest.TestCase):
    def test_get_csv_row(self):
        expected = {"text": "text", "link": "link"}
        self.assertEqual(get_csv_row(text="text", link="link"), expected)

    def test_fail_get_csv_row(self):
        with self.assertRaises(TypeError):
            get_csv_row(text="text")


if __name__ == "__main__":
    unittest.main()
