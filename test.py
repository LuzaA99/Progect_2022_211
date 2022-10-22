from unittest import TestCase


def return_random_str_for_test(filename: str, idx) -> str:
    with open(filename) as fin:
        file = list(map(str.strip, fin))
        return file[idx]

class TestCaseMovie1(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "5;Father of the Bride Part II (1995);Comedy", return_random_str_for_test("/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv", 6))


class TestCaseMovie2(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "732;His Girl Friday (1940);Comedy|Romance", return_random_str_for_test("/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv", 733))

class TestCaseMovie3(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "732;His Girl Friday (1940);Comedy|Romance", return_random_str_for_test("/Users/lizaakopova/PycharmProjects/pythonProject1/movies22.csv", 732))



class TestCaseSerial1(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "Trinkets;Coming Of Age Drama;2;20", return_random_str_for_test("/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv", 241))

class TestCaseSerial2(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "Ethos;Drama;1;8", return_random_str_for_test("/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv", 149))

class TestCaseSerial3(TestCase):

    def test_random_str(self):
        self.assertEqual(
            "The Crown;Historical Drama;4;40", return_random_str_for_test("/Users/lizaakopova/PycharmProjects/pythonProject1/tv_shows_data.csv", 4))
