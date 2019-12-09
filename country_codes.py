# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:43:35 2019

@author: user
"""

#from pygal.i18n import COUNTRIES # Коды стран хранятся в модуле i18n (internalization)
'''Оказалось что из pygal 2 изъяли список стран и модуль i18n, поэтому устанавливаем pygal_maps_world и берем от туда'''
# You can install that with pip install pygal_maps_world. from pygal.maps.world import COUNTRIES:

# from pygal_maps_world import i18n

from pygal_maps_world.i18n import COUNTRIES
'''
В словаре COUNTRIES двухбуквенные кодыPygal стран являются ключами, а названия
стран — значениями. Чтобы просмотреть коды, импортируйте словарь из модуля
i18n и выведите его ключи и значения:
'''
# Сортировка в алфавитном порядке стран и выыод их названий и ключей:
#for country_code in sorted(COUNTRIES.key()):
#    print(country_code, COUNTRIES[country_code])
def get_country_code(country_name):
    '''Возвращает для заданной страны её код Pygal, состоящий из даух букв.'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # Если страна не найдена, вернуть None.
        
    return None
if __name__ == "__main__":    
    print(get_country_code('Andorra'))
    print(get_country_code('Bahrain'))
    print(get_country_code('Afghanistan'))