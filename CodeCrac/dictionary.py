# # Записывыем словарь
# my_dict = {"name" : "Elbol", "age" : 32, "city" : "Shengel'dy"} # создания словаря

# # Открываем файлы для записи
# file = open("file.txt", "w", encoding='utf8')

# # Запись словаря в файл
# for key, value in my_dict.items():
#     file.write(f"{key}: {value}\n")

# # Закрытия файла
# file.close()        

# # +++++++++++++++++++++++++++++


# countries={ 
# 'Нігерія':{'cw': 'Нігерія','sq': '923768','sq':'195900000','ct':'Африка' },
# 'Німеччина':{'cw': 'Німеччина','sq': '357578','sq':'83000000','ct':'Європа'},
# 'Пакистан':{'cw': 'Пакистан','sq': '803950','sq':'187300000','ct':'Азія'},
# 'Італія':{'cw': 'Італія','sq': '301000','sq':'60600000','ct':'Європа'},
# 'Узбекистан':{'cw': 'Узбекистан','sq': '447400','sq':'31100500','ct':'Азія'},
# 'Франція':{'cw': 'Франція','sq': '643801','sq':'66990000','ct':'Європа'},
# 'Палестина':{'cw': 'Палестина','sq': '6220','sq':'5159000','ct':'Азія'},
# 'Ніґер':{'cw': 'Ніґер','sq': '1267000','sq':'22400000','ct':'Африка'},
# 'Україна':{'cw': 'Україна','sq': '603628','sq':'41980000','ct':'Європа'},
# 'Греція':{'cw': 'Греція','sq': '131957','sq':'10760000','ct':'Європа'}
#             }

# for country in countries:
#     if 'Африка' or "Азія" in country:
#         print(country)
#     else:
#         print("-")


# +++++++++++++++++++++++++++++++++++++++++++


students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "Dave": "B",
    "Eve": "A"
}

target_grade = "B"

keys = [key for key, value in students.items() if value == target_grade]

print("Keys with target grade:", keys)


# ++++++++++++++++++++++++

