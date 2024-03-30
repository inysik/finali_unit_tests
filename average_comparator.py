class AverageComparator:
    def __init__(self, list1, list2):
        self.list1 = list1  
        self.list2 = list2  

    def calculate_average(self, lst):
        if not lst:  
            return 0
        return sum(lst) / len(lst)  

    def compare_averages(self):
        average1 = self.calculate_average(self.list1)  
        average2 = self.calculate_average(self.list2) 

        if average1 > average2:  # Сравнение средних значений
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

# Пример 
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5] 
    list2 = [6, 7, 8, 9, 10] 

    comparator = AverageComparator(list1, list2) 
    result = comparator.compare_averages()  
    print(result)  
