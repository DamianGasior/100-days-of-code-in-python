def filter_even(numbers):
    """Zwraca tylko liczby parzyste z listy."""
    return [n for n in numbers if n % 2 == 0]

def word_count(words):
    """Zwraca słownik {słowo: liczba wystąpień}."""
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def merge_dicts(d1, d2):
    """Łączy dwa słowniki, wartości z d2 nadpisują wartości z d1."""
    merged = d1.copy()
    merged.update(d2)
    return merged


my_sample_numbers=[0,1,2,3,4,5,6,7,8,9,10]
print(filter_even(my_sample_numbers))
print(word_count("Nie można dzielić przez zero!"))

one_dict={ "Wroclaw":1,"Krakow":2,"Warszawa":3 }
second_dict={ "Lato":12,"Zima":345,"Jesien":678 }


print(merge_dicts(one_dict,second_dict))

