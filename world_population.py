# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:13:36 2019

Pygal для работы
с географическими данными,
 мы построим визуализации, отражающие распределение населения по странам
"""
import json, pygal
from pygal.style import DarkColorizedStyle, LightColorizedStyle, RotateStyle
from country_codes import get_country_code
       
# Список заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_populations ={}
# Вывод населения каждой страны за 2010 год.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
# Групировка стран по 3 уровням населения
cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{} 
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
        

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'Популяция в 2010'
wm.add('до 10-милионов',cc_pops_1)
wm.add('до 1миллиарда',cc_pops_2)
wm.add('более 1-миллиарда',cc_pops_3)

wm.render_to_file('world_population.svg')