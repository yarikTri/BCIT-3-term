# РК1, Ярослав Кузьмин, ИУ5-32Б, Вариант Б-14.
# (Ира по привычке сделала 13-й вариант, как по журналу, и попросила меня сделать её вариант)

# Запросы:
# 1. «CD-диск» и «CD-библиотека» связаны соотношением один-ко-многим.
# Выведите список всех связанных дисков и библиотек,
# отсортированный по именам дисков, сортировка по библиотекам произвольная.
# 2. «CD-диск» и «CD-библиотека» связаны соотношением один-ко-многим.
# Выведите список библиотек со средним годом выпуска дисков в каждой библиотеке,
# отсортированный по среднему году выпуска дисков.
# 3. «CD-диск» и «CD-библиотека» связаны соотношением многие-ко-многим.
# Выведите список всех дисков, у которых заголовок заканчивается на «и», и названия их библиотек.

# используется для сортировки
from operator import itemgetter

class Disk:
    """CD-диск"""
    def __init__(self, id, title, year, lib_id):
        self.id = id
        self.title = title
        self.year = year
        self.lib_id = lib_id
 
class Lib:
    """CD-библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DiskLib:
    """
    'CD-диски в библиотеке' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, disk_id, lib_id):
        self.disk_id = disk_id
        self.lib_id = lib_id

# CD-диски
disks = [
    Disk(1, "Финал ЛЧ: Челси - Ман Сити", 2020, 1),
    Disk(2, "Кузьмины свадьба", 2002, 2),
    Disk(3, "Цой концерт Мск", 1986, 2),
    Disk(4, "Смешарики новые серии", 2009, 2),
    Disk(5, "Лекция 3 БКИТ МГТУ ИУ5", 2022, 3),
]

# CD-библиотеки
libs = [
    Lib(1, "Государственная"),
    Lib(2, "Частная"),
    Lib(3, "Бауманская"),
]

disks_libs = [
    DiskLib(1, 1),
    DiskLib(2, 2),
    DiskLib(3, 2),
    DiskLib(4, 2),
    DiskLib(5, 3),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(d.title, d.year, l.name)
        for d in disks
        for l in libs
        if d.lib_id == l.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, dl.lib_id, dl.disk_id) 
        for l in libs 
        for dl in disks_libs 
        if l.id == dl.lib_id]
    
    many_to_many = [(d.title, d.year, lib_name) 
        for lib_name, lib_id, disk_id in many_to_many_temp
        for d in disks if d.id == disk_id]
 
    print("Задание Б1")
    res_11 = sorted(one_to_many, key = itemgetter(0))
    print(res_11)
    
    print("\nЗадание Б2")
    res_12_unsorted = []

    # Перебираем все библиотеки
    for l in libs:
        # Список дисков библиотеки
        l_disks = list(filter(lambda i: i[2] == l.name, one_to_many))
        # Если библиотека не пустая        
        if len(l_disks) > 0:
            # Год диска библиотеки
            l_years = [year for _ , year , _ in l_disks]
            # Сумма годов дисков библиотеки
            l_years_sum = sum(l_years)
            res_12_unsorted.append((l.name, int(l_years_sum / len(l_disks))))
 
    # Сортировка по суммарному году
    res_12 = sorted(res_12_unsorted, key = itemgetter(1), reverse = False)
    print(res_12)
 
    print("\nЗадание Б3")
    res_13 = []
    # Перебираем все бибилиотеки
    for d in disks:
        if d.title[-1] != 'и':
            continue
        for l in libs:
            if l.id == d.lib_id:
                res_13.append((d.title, l.name))
                break
 
    print(res_13)
 
if __name__ == "__main__":
    main()
