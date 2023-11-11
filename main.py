import json
import pandas as pd
import os
import requests

directory = "/root/SPk1_worlds/world/stats" #указываешь директорию
files = []
files += os.listdir(directory)
files.sort()

nicknames_path = 'nicknames.json'

nicknames: dict = json.loads(open(nicknames_path,'r+').read()) if os.path.exists(nicknames_path) else dict()

stats = [
    {'UUID':'UserNickname'},
    {'Время в игре':'custom:play_one_minute'},
    {'Кол-во смертей':'custom:deaths'},
    {'Выбрашено предметов':'custom:drop'},
    {'Выведено животных':'custom:animals_bred'},
    {'Зачарованно предметов':'custom:enchant_item'},
    {'Крался':'custom:sneak_time'},
    {'Нанесено урона':'custom:damage_dealt'},
    {'Поймано рыбы':'custom:fish_caught'},
    {'Получено урона':'custom:damage_taken'},
    {'Преодолено бегом':'custom:sprint_one_cm'},
    {'Преодолено в полёте':'custom:fly_one_cm'},
    {'Преодолено вплавь':'custom:swim_one_cm'},
    {'Преодолено на элитрах':'custom:aviate_one_cm'},
    {'Прыжков':'custom:jump'},
    {'Съедено кусков торта':'custom:eat_cake_slice'},
    {'Убито игроков':'custom:player_kills'},
    {'Убито существ':'custom:mob_kills'},
    {'Создано - маяк':'crafted:beacon'},
    {'Создано - деревянных дверей':'crafted:oak_door'},
    {'Создано верстаков':'crafted:crafting_table'},
    {'Добыто - алмазов':'mined:diamond_ore'},
    {'Добыто - незерита':'mined:ancient_debris'},
    {'Добыто - лазуритовой руды':'mined:lapis_ore'},
    {'Добыто - изумрудная руда':'mined:emerald_ore'},
    {'Добыто - редстоуновая руда':'mined:redstone_ore'},
    {'Добыто - золотая руда':'mined:gold_ore'},
    {'Добыто - железная руда':'mined:iron_ore'},
    {'Добыто - угольная руда':'mined:coal_ore'},
    {'Добыто - камня':'mined:stone'},
    {'Добыто - обсидиан':'mined:obsidian'},
    {'Добыто - дубовое бревно':'mined:oak_log'},
    {'Съедено - золотое зачарованное яблоко':'used:enchanted_golden_apple'},
    {'Убито - Всполохо':'killed:blaze'},
    {'Убито - пауков':'killed:spider'},
    {'Убито - зомби':'killed:zombie'},
    {'Убито - куриц':'killed:chicken'},
    {'Убито - крипер':'killed:creeper'},
    {'Убито - коров':'killed:cow'},
    {'Убито - эндер-дракон':'killed:ender_dragon'},
    {'Убито - эндермен':'killed:enderman'},
    {'Убито - Гаст':'killed:ghast'},
    {'Убито - овец':'killed:sheep'},
    {'Убито - шалкера':'killed:shulker'},
    {'Убито - скелетов':'killed:skeleton'},
    {'Убито - слаймов':'killed:slime'},
    {'Убито - визер скелетов':'killed:wither_skeleton'},
    {'Убито - визеров':'killed:wither'}
]

statistic = pd.DataFrame(columns=[[key for key in stat][0] for stat in stats])

for i, file in enumerate(files):
    uuid = file[:-5]
    with open(directory+'/'+file) as f:
        user_stats = json.load(f).get('stats',{})
    row = []
    
    if nicknames.get(uuid):
        nickname = nicknames.get(uuid)
    else:
        url = 'https://api.mojang.com/user/profile/'+uuid
        nickname = requests.get(url).json().get('name',uuid)
        nicknames[uuid] = nickname
        json.dump(nicknames,open(nicknames_path,'w+'),ensure_ascii=False,indent=4)

    for stat in stats:
        key = [value for value in stat.values()][0]
        if key == 'UserNickname':
            row.append(nickname)
        else:
            category, stat_name = key.split(':')
            user_stat = user_stats.get(f'minecraft:{category}',{}).get(f'minecraft:{stat_name}')
            if user_stat:
                value = int(user_stat)
                if stat_name == 'play_one_minute':
                    value = value/20/60/60
                row.append(value)
            else:
                row.append(0)

    
    statistic.loc[len(statistic.index)] = row
    print(f'[{i+1}/{len(files)}]',nickname,file)

print(len(row))
print(statistic)


statistic.to_excel('test.xlsx')
