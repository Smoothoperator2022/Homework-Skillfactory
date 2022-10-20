"""  Counter  """
from collections import Counter
# Создаём пустой объект Counter
c = Counter() #Теперь в переменной c хранится объект с возможностями Counter.
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']

c = Counter()
for car in cars:
    c[car] += 1
 
print(c)
#Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
c = Counter(cars)
print(c)
# Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
print (c['purple'])
#0
print(c['black'])
#3
print(c.values())
#dict_values([3, 2, 3, 1])
print(sum(c.values()))
#9
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
# Counter({'black': 4, 'yellow': 3, 'white': 2})
print(counter_spb)
# Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
print(counter_moscow + counter_spb)
# Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})
"""Чтобы узнать разницу между объектами Counter, 
необходимо воспользоваться функцией subtract, 
которая меняет тот объект, к которому применяется. 
В примере выше из значений, посчитанных для Москвы, 
вычитаются значения, посчитанные для Санкт-Петербурга:"""
print(counter_moscow)
print(counter_spb)
# Counter({'black': 4, 'yellow': 3, 'white': 2})
# Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
 
counter_moscow.subtract(counter_spb)
print(counter_moscow)
# Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})
"""Заметьте, что белых машин в counter_spb оказалось больше, чем в counter_moscow, 
поэтому разность отрицательная. Красных машин в moscow вообще не было,
а в spb их оказалось сразу две, поэтому разница равна -2. 
Значения для black и yellow остались положительными, потому что их было больше."""
# Пересоздаём счётчики, потому что объект counter_moscow поменял свои значения
# после функции subtract.
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})
print(*counter_moscow.elements())
#black black black black white white yellow yellow yellow
print(list(counter_moscow))
#['black', 'white', 'yellow']
print(counter_moscow.most_common())
# [('black', 4), ('yellow', 3), ('white', 2)]
print(counter_moscow.most_common(2))
# [('black', 4), ('yellow', 3)]
counter_moscow.clear()
print(counter_moscow)
# Counter()
