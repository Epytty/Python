import pandas as pd

# Создаем DataFrame с продажами по дням недели
sales = pd.DataFrame({
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday'],
    'apple_pie': [10, 20, 15, 5],
    'cherry_pie': [5, 10, 20, 15],
    'blueberry_pie': [15, 5, 10, 20]
})

# Суммируем продажи по дням недели
sales_by_day = sales.sum()

# Выводим результат
print(sales_by_day)