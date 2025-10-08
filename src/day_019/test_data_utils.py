import pytest
import data_utils


@pytest.fixture
def my_sample_numbers():
    return [0,1,2,3,4,5,6,7,8,9,10]


# my_sample_numbers=[0,1,2,3,4,5,6,7,8,9,10]

def test_filter_even(my_sample_numbers):
    assert data_utils.filter_even(my_sample_numbers)==[0, 2, 4, 6, 8, 10]


# 2. Użycie fixture w teście
# def test_filter_even(my_sample_numbers):
#     assert data_utils.filter_even(my_sample_numbers) == [0, 2, 4, 6, 8, 10]


# Tutaj my_sample_numbers w nawiasie nie oznacza, że wywołujesz funkcję.
# To tylko nazwa parametru testu, która musi się zgadzać z nazwą fixture.

# Pytest patrzy: „Ooo, test test_filter_even wymaga argumentu o nazwie my_sample_numbers. Mam taką fixture zarejestrowaną. To ja ją odpalę i zwrócę listę [0,...,10].”

# Czyli efekt końcowy wygląda tak, jakbyś napisał:

# def test_filter_even():
#     data = [0,1,2,3,4,5,6,7,8,9,10]   # <-- pytest zrobił to za Ciebie
#     assert data_utils.filter_even(data) == [0, 2, 4, 6, 8, 10]

@pytest.fixture
def my_sample_text():
    return "Nie można dzielić przez zero!"

def test_word_count(my_sample_text):
    assert data_utils.word_count(my_sample_text)=={'N': 1, 'i': 3, 'e': 4, ' ': 4, 'm': 1, 'o': 2, 'ż': 1, 'n': 1, 'a': 1, 'd': 1, 'z': 4, 'l': 1, 'ć': 1, 'p': 1, 'r': 2, '!': 1}


@pytest.fixture
def one_dict():
    one_dict={ "Wroclaw":1,"Krakow":2,"Warszawa":3 }
    return one_dict

@pytest.fixture
def second_dict():
    second_dict={ "Lato":12,"Zima":345,"Jesien":678 }
    return second_dict



def test_merge_dict(one_dict,second_dict):
    print(type(one_dict))
    print(type(second_dict))

    assert data_utils.merge_dicts(one_dict,second_dict)=={'Wroclaw': 1, 'Krakow': 2, 'Warszawa': 3, 'Lato': 12, 'Zima': 345, 'Jesien': 678}