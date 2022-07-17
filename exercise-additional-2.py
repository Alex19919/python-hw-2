# Напишіть функцію commonStr що задовільняє наступній умові:



# Дано дві строчки, поверніть нову строчку 
# яка буде складатись виключно зі спільних символів перерадних строк.
# Якщо немає спільних символів - поверніть пусту строчку. 
# Ви можете повернути відповідь у будь-якому порядку.
# Символи не повині дублюватись у відповіді.

# Приклад 1
# commonStr('loli', 'luck') -> 'l'

# Приклад 1
# commonStr('good day', 'good morning') -> 'god'


# def commonStr(str1, str2):
#     return ''

# print(commonStr('loli', 'luck') == 'l') 
# print(commonStr('good day', 'good morning') == 'god') 


def commonStr(str1, str2):
    start = set(str1).intersection(set(str2))
    end = ''
    for x in start:
        end += x
    print(end)
    return end


print(commonStr('loli', 'luck') == 'l')
print(commonStr('good day', 'good morning') == 'god')




# повністю не розібрався ...приклади  переглядав на сайтах