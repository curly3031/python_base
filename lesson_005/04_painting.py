#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Создать пакет, в котором собрать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Каждую функцию разместить в своем модуле. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


import simple_draw as sd
from painting import smile as pt_smile, \
                     snowfall as pt_snowfall, \
                     wall as pt_wall, \
                     tree as pt_tree, \
                     rainbow as pt_rainbow, \
                     sun as pt_sun

sd.resolution = (1200, 800)

global background_color
background_color = sd.COLOR_BLACK
sd.background_color = background_color


pt_snowfall.snowflakes_count = 30
snow_falling = True
snowflakes = {}
snowflakes_remove = {}

part_of_day = ''

tick = 0

building_size = (400, 200)
building_start_point = sd.get_point(x=100, y=10)

root_point = ((sd.get_point(750, 30),  building_size[1] / 1.5 - sd.random_number(10, 30)),
              # (sd.get_point(800, 30),  building_size[1] / 2 - sd.random_number(10, 30)),
              (sd.get_point(1100, 30), building_size[1] / 2 - sd.random_number(10, 30)),
              # (sd.get_point(100, 30),  building_size[1] / 2 - sd.random_number(10, 30)),
              (sd.get_point(900, 30),  building_size[1] / 2 - sd.random_number(10, 30)))

pt_wall.wall_size = building_size

roof_point_list = [sd.get_point
                   (building_start_point.x+1,
                    building_start_point.y+1 + building_size[1]),

                   sd.get_point
                   (building_start_point.x+1 + building_size[0] // 2,
                    building_start_point.y+1 + building_size[1] + building_size[1]),

                   sd.get_point
                   (building_start_point.x+1 + building_size[0],
                    building_start_point.y+1 + building_size[1]),
                   ]


def draw_ground():
    # рисуем землю
    sd.rectangle(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 40), sd.COLOR_DARK_ORANGE)
    grass_count = 1
    #
    # for i in range(grass_count):
    #     x = sd.random_number(1, sd.resolution[0])
    #     y = sd.random_number(40, 41)
    #     sd.vector(start=sd.get_point(x, y), angle=90, length=sd.random_number(1, 8), color=sd.COLOR_DARK_GREEN, width=3)


def draw_house():

    # рисуем стену здания
    pt_wall.draw_wall(pos_x=building_start_point.x, pos_y=building_start_point.y)

    # рисуем крышу здания
    sd.polygon(point_list=roof_point_list, color=sd.COLOR_DARK_GREEN, width=0)
    sd.polygon(point_list=roof_point_list, color=sd.COLOR_BLACK, width=1)

    # рисуем окно на крыше
    sd.circle(sd.get_point(building_start_point.x+1 + building_size[0]//2,
                           building_start_point.y + 1 + building_size[1] + building_size[1] // 2),
              30, color=sd.COLOR_DARK_YELLOW, width=0)

    sd.circle(sd.get_point(building_start_point.x+1 + building_size[0]//2,
                           building_start_point.y + 1 + building_size[1] + building_size[1] // 2),
              30, color=sd.COLOR_BLACK, width=1)

    # рисуем окно здания
    x_step = building_size[0] // 4
    y_step = building_size[1] // 5

    sd.rectangle(sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
                 sd.get_point(building_start_point.x+1 + building_size[0] - x_step,
                              building_start_point.y+1 + building_size[1] - y_step),
                 color=sd.COLOR_DARK_YELLOW, width=0)

    sd.rectangle(sd.get_point(building_start_point.x+1 + x_step, building_start_point.y+1 + y_step),
                 sd.get_point(building_start_point.x+1 + building_size[0] - x_step,
                              building_start_point.y+1 + building_size[1] - y_step),
                 color=sd.COLOR_BLACK, width=3)


def change_part_day():
    global part_of_day, background_color

    if tick == 0:
        background_color = (109, 147, 176)
        part_of_day = 'morning'

    # elif tick == 100:
    #     background_color = (51, 51, 51)
    # elif tick == 150:
    #     background_color = (65, 96, 120)
    # elif tick == 200:
    #     background_color = (33, 44, 100)
    #
    # elif tick == 300:
    #     background_color = (24, 217, 255)
    #     part_of_day = 'afternoon'
    #
    # elif tick == 500:
    #     background_color = (209, 221, 230)
    #     part_of_day = 'evening'
    # # elif tick == 550:
    # #     background_color = (109, 147, 176)
    # # elif tick == 600:
    # #     background_color = (65, 96, 120)
    # # elif tick == 750:
    # #     background_color = (51, 51, 51)
    # elif tick == 800:
    #     background_color = sd.COLOR_BLACK
    #     part_of_day = 'night'

    if sd.background_color != background_color:
        sd.background_color = background_color
        pt_snowfall.background_color = background_color
        sd.clear_screen()

step = 0


while True:

    if tick >= 800:
        tick = 0

    sd.start_drawing()

    pt_sun.draw_sun(sd.get_point(100,600), 40, 100, 20)
    change_part_day()

    print(part_of_day)
    if part_of_day in ('night', 'evening'):
        snow_falling = True
        step = 0
    elif part_of_day in ('morning'):
        if tick % 24 == 0:
            # sd.clear_screen()
            step += 24
        pt_rainbow.draw_rainbow(x=750, y=100, radius=400, width=10, game_tick=tick, grow_step=step)
        snow_falling = False
    elif part_of_day in ('afternoon'):
        pt_rainbow.draw_rainbow(x=750, y=100, radius=700, width=10, game_tick=tick, )
    # else:
    #     pt_rainbow.draw_rainbow(x=750, y=100, radius=900, width=6, game_tick=tick, )

    pt_snowfall.draw_snowflake(roof_point_list, falling=snow_falling)

    # удаление снежинок из словаря
    snowflakes = {k: v for k, v in snowflakes.items() if k not in snowflakes_remove}

    draw_ground()
    draw_house()

    for root_param in root_point:
        pt_tree.draw_simetric_branches(point=root_param[0], angle=90, length=root_param[1], set_day=part_of_day)

    pt_smile.draw_smile(building_start_point.x + 1 + building_size[0] // 2,
                        building_start_point.y + 1 + building_size[1] // 2,
                        tick)

    # sd.sleep(0.03)

    tick += 1

    sd.finish_drawing()

    if sd.user_want_exit():
        break