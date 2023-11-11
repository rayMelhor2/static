import json
import pandas as pd
import os
import requests

directory = "/root/SPk1_worlds/world/stats" #указываешь директорию
files = []
files += os.listdir(directory)
files.sort()

nicknames_path = 'nicknames.json'

nicknames: dict = json.loads(open(nicknames_path,'r+').read())

statistic = pd.DataFrame(columns=[
    'UUID',
    'Время в игре',
    'Кол-во смертей',
    'Выбрашено предметов',
    'Выведено животных',
    'Зачарованно предметов',
    'Крался',
    'Нанесено урона',
    'Поймано рыбы',
    'Получено урона',
    'Преодолено бегом',
    'Преодолено в полёте',
    'Преодолено вплавь',
    'Преодолено на элитрах',
    'Прыжков',
    'Съедено кусков торта',
    'Убито игроков',
    'Убито существ',
    'Создано - маяк',
    'Создано - деревянных дверей',
    'Создано верстаков',
    'Добыто - алмазов',
    'Добыто - незерита',
    'Добыто - лазуритовой руды',
    'Добыто - изумрудная руда',
    'Добыто - редстоуновая руда',
    'Добыто - золотая руда',
    'Добыто - железная руда',
    'Добыто - угольная руда',
    'Добыто - камня',
    'Добыто - обсидиан',
    'Добыто - дубовое бревно',
    'Съедено - золотое зачарованное яблоко',
    'Убито - Всполохо',
    'Убито - пауков',
    'Убито - зомби',
    'Убито - куриц',
    'Убито - крипер',
    'Убито - коров',
    'Убито - эндер-дракон',
    'Убито - эндермен',
    'Убито - Гаст',
    'Убито - овец',
    'Убито - шалкера',
    'Убито - скелетов',
    'Убито - слаймов',
    'Убито - визер скелетов',
    'Убито - визеров'
])

for i, file in enumerate(files):
    uuid = file[:-5]
    with open(directory+'/'+file) as f:
        templates = json.load(f)
    row=[]
    url = 'https://api.mojang.com/user/profile/'+uuid
    if nicknames.get(uuid):
        nickname = nicknames.get(uuid)
    else:
        nickname = requests.get(url).json().get('name',uuid)
        nicknames[uuid] = nickname
        json.dump(nicknames,open(nicknames_path,'w+'),ensure_ascii=False,indent=4)
    row.append(nickname)

    if not templates['stats']['minecraft:custom'].get('minecraft:play_one_minute'):
        row.append(0)
    else:
        row.append(int(templates['stats']['minecraft:custom']['minecraft:play_one_minute'])/20/60/60)

    if not templates['stats']['minecraft:custom'].get('minecraft:deaths'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:deaths'])

    if not templates['stats']['minecraft:custom'].get('minecraft:drop'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:drop'])

    if not templates['stats']['minecraft:custom'].get('minecraft:animals_bred'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:animals_bred'])

    if not templates['stats']['minecraft:custom'].get('minecraft:enchant_item'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:enchant_item'])

    if not templates['stats']['minecraft:custom'].get('minecraft:sneak_time'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:sneak_time'])

    if not templates['stats']['minecraft:custom'].get('minecraft:damage_dealt'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:damage_dealt'])

    if not templates['stats']['minecraft:custom'].get('minecraft:fish_caught'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:fish_caught'])

    if not templates['stats']['minecraft:custom'].get('minecraft:damage_taken'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:damage_taken'])

    if not templates['stats']['minecraft:custom'].get('minecraft:sprint_one_cm'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:sprint_one_cm'])

    if not templates['stats']['minecraft:custom'].get('minecraft:fly_one_cm'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:fly_one_cm'])

    if not templates['stats']['minecraft:custom'].get('minecraft:swim_one_cm'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:swim_one_cm'])

    if not templates['stats']['minecraft:custom'].get('minecraft:aviate_one_cm'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:aviate_one_cm'])

    if not templates['stats']['minecraft:custom'].get('minecraft:jump'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:jump'])

    if not templates['stats']['minecraft:custom'].get('minecraft:eat_cake_slice'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:eat_cake_slice'])

    if not templates['stats']['minecraft:custom'].get('minecraft:player_kills'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:player_kills'])

    if not templates['stats']['minecraft:custom'].get('minecraft:mob_kills'):
        row.append(0)
    else:
        row.append(templates['stats']['minecraft:custom']['minecraft:mob_kills'])

    if not templates['stats'].get('minecraft:crafted'):
        row.append(0)
    else:
        if templates['stats']['minecraft:crafted'].get('minecraft:beacon'):
            row.append(templates['stats']['minecraft:crafted']['minecraft:beacon'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:crafted'):
        row.append(0)
    else:
        if templates['stats']['minecraft:crafted'].get('minecraft:oak_door'):
            row.append(templates['stats']['minecraft:crafted']['minecraft:oak_door'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:crafted'):
        row.append(0)
    else:
        if templates['stats']['minecraft:crafted'].get('minecraft:crafting_table'):
            row.append(templates['stats']['minecraft:crafted']['minecraft:crafting_table'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:diamond_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:diamond_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:ancient_debris'):
            row.append(templates['stats']['minecraft:mined']['minecraft:ancient_debris'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:lapis_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:lapis_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:emerald_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:emerald_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:redstone_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:redstone_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:gold_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:gold_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:iron_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:iron_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:coal_ore'):
            row.append(templates['stats']['minecraft:mined']['minecraft:coal_ore'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:stone'):
            row.append(templates['stats']['minecraft:mined']['minecraft:stone'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:obsidian'):
            row.append(templates['stats']['minecraft:mined']['minecraft:obsidian'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:mined'):
        row.append(0)
    else:
        if templates['stats']['minecraft:mined'].get('minecraft:oak_log'):
            row.append(templates['stats']['minecraft:mined']['minecraft:oak_log'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:used'):
        row.append(0)
    else:
        if templates['stats']['minecraft:used'].get('minecraft:enchanted_golden_apple'):
            row.append(templates['stats']['minecraft:used']['minecraft:enchanted_golden_apple'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:blaze'):
            row.append(templates['stats']['minecraft:killed']['minecraft:blaze'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:spider'):
            row.append(templates['stats']['minecraft:killed']['minecraft:spider'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:zombie'):
            row.append(templates['stats']['minecraft:killed']['minecraft:zombie'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:chicken'):
            row.append(templates['stats']['minecraft:killed']['minecraft:chicken'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:creeper'):
            row.append(templates['stats']['minecraft:killed']['minecraft:creeper'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:cow'):
            row.append(templates['stats']['minecraft:killed']['minecraft:cow'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:ender_dragon'):
            row.append(templates['stats']['minecraft:killed']['minecraft:ender_dragon'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:enderman'):
            row.append(templates['stats']['minecraft:killed']['minecraft:enderman'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:ghast'):
            row.append(templates['stats']['minecraft:killed']['minecraft:ghast'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:sheep'):
            row.append(templates['stats']['minecraft:killed']['minecraft:sheep'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:shulker'):
            row.append(templates['stats']['minecraft:killed']['minecraft:shulker'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:skeleton'):
            row.append(templates['stats']['minecraft:killed']['minecraft:skeleton'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:slime'):
            row.append(templates['stats']['minecraft:killed']['minecraft:slime'])
        else:
            row.append(0)


    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:wither_skeleton'):
            row.append(templates['stats']['minecraft:killed']['minecraft:wither_skeleton'])
        else:
            row.append(0)

    if not templates['stats'].get('minecraft:killed'):
        row.append(0)
    else:
        if templates['stats']['minecraft:killed'].get('minecraft:wither'):
            row.append(templates['stats']['minecraft:killed']['minecraft:wither'])
        else:
            row.append(0)
    
    statistic.loc[len(statistic.index)] = row
    print(f'[{i}/{len(files)}]',nickname,file)

print(len(row))
print(statistic)


statistic.to_excel('test.xlsx')
