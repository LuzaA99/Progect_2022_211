from unittest import TestCase


def return_random_str(filename: str, idx) -> str:
    with open(filename) as fin:
        file = list(map(str.strip, fin))
        return file[idx]


class TestCaseMovie(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "5;Father of the Bride Part II (1995);Comedy", return_random_str("/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv", 6))

    def test_random_str2(self):
        self.assertEqual(
            "732;His Girl Friday (1940);Comedy|Romance", return_random_str("/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv", 733))

    def test_random_str3(self):
        self.assertEqual(
            "732;His Girl Friday (1940);Comedy|Romance", return_random_str("/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv", 732))


class TestCaseSerial(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "Trinkets;Coming Of Age Drama;2;20", return_random_str("/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv", 241))

    def test_random_str2(self):
        self.assertEqual(
            "Ethos;Drama;1;8", return_random_str("/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv", 149))

    def test_random_str3(self):
        self.assertEqual(
            "The Crown;Historical Drama;4;40", return_random_str("/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv", 4))
