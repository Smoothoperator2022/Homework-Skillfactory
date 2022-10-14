"""  defaultdict  """
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
#Сохраним эти данные в словаре, в котором ключами будут номера групп, а элементами — списки студентов.
# Сделать это можно следующим образом:

groups = dict()
 
for student, group in students:
    # Проверяем, есть ли уже эта группа в словаре
    if group not in groups:
        # Если группы ещё нет в словаре, создаём для неё пустой список
        groups[group] = list()
    groups[group].append(student)
 
print(groups)
# {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']}

#В данном коде в цикле for происходит распаковка кортежа: в переменные цикла student и group 
# попадают первый и второй элементы кортежей из списка students. То есть на первой итерации цикла 
# в переменной student содержится строка 'Ivanov', а в переменной group — целое число 1. 
# На второй итерации цикла в переменной student содержится строка 'Smirnov',
# а в переменной group — целое число 4. И так далее.
#Обратите внимание, что для решения этой задачи нам потребовался шаг 
# с проверкой наличия номера группы в словаре. Если номера группы не было, для этой группы мы 
# создавали новый список в словаре. Без шага проверки мы бы натолкнулись на KeyError:
groups = dict()
 
for student, group in students:
    groups[group].append(student)
 
print(groups)
# KeyError: 1
#Создадим defaultdict, в котором при обращении по несуществующему ключу будет автоматически создаваться новый список.
# Для этого при создании объекта defaultdict в круглых скобках передадим параметр list:

from collections import defaultdict
groups = defaultdict(list)
#Обратите внимание, что в скобках мы передаём именно указатель на класс объекта 
# (например list; также можно было бы применить set, dict) без круглых скобок,
# которые используются для создания нового экземпляра объекта.
#Теперь тот же код, который вызывал ошибку при работе с обычным словарём, сработает так, как ожидается:
for student, group in students:
    groups[group].append(student)
 
print(groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})
#В выводе есть небольшое отличие от обычного словаря: печатаются не только элементы словаря, но и само название объекта defaultdict, 
#а также класс объекта, который задан по умолчанию. В данном случае это <class 'list'>. 
#Получить элемент из defaultdict по ключу можно так же, как и из обычного словаря:
print(groups[3])
# ['Petrov', 'Markov']
#Если запрашиваемого ключа нет в словаре, KeyError не возникнет. Вместо этого будет напечатан пустой элемент, который создаётся в словаре по умолчанию:
print(groups[2021])
# []
#Теперь в словаре groups автоматически появился элемент 2021 с пустым списком внутри, 
# несмотря на то что мы его не создавали:
print(groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov'], 2021: []})
#Итак, вы обратили внимание, что поведение defaultdict в коде отличается от обычного словаря dict.
# Узнать, с каким именно словарём мы имеем дело в коде, можно с помощью встроенной функции type:
dict_object = dict()
defaultdict_object = defaultdict()
 
print(type(dict_object))
# <class 'dict'>
print(type(defaultdict_object))
# <class 'collections.defaultdict'>
#Видно, что типы переменных dict_object и defaultdict_object отличаются.
print(dict_object)
# {}
print(defaultdict_object)
# defaultdict(None, {})
#Заметьте, что в этом примере мы не задавали объект, который по умолчанию хранится в экземпляре defaultdict, 
# поэтому объектом по умолчанию является None.