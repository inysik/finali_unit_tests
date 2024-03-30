from average_comparator import AverageComparator



def test_compare_averages_first_greater():
    comparator = AverageComparator([1, 2, 3], [1, 2])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_compare_averages_second_greater():
    comparator = AverageComparator([1, 2], [1, 2, 3])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    comparator = AverageComparator([1, 2, 3], [3, 2, 1])
    assert comparator.compare_averages() == "Средние значения равны"

def test_compare_averages_first_empty():
    comparator = AverageComparator([], [1, 2, 3])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_compare_averages_second_empty():
    comparator = AverageComparator([1, 2, 3], [])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_compare_averages_both_empty():
    comparator = AverageComparator([], [])
    assert comparator.compare_averages() == "Средние значения равны"

def test_compare_averages_first_negative():
    comparator = AverageComparator([-1, -2, -3], [1, 2, 3])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_compare_averages_second_negative():
    comparator = AverageComparator([1, 2, 3], [-1, -2, -3])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_compare_averages_both_negative():
    comparator = AverageComparator([-1, -2, -3], [-1, -2, -3])
    assert comparator.compare_averages() == "Средние значения равны"
