from models.aircraft import Aircraft
from models.attack import Attack
from models.pilots import Pilot
from models.targets import Targets
from files_actions import read_json
from weather_api import read_location


def main_menu():
    """
    this function is used to display the main menu for the air strike simulation
    :return: null
    """
    print('welcome to air strike simulation!'
          '\n - Click 1 upload target fighter and pilot from JSON files.'
          '\n - Click 2 to show all target recommendations.'
          '\n - Click 3 to save all target recommendations to csv file.'
          '\n - Click 4 to quit.')

    select_user = int(input('\nSelect an option: '))
    while True:
        match select_user:
            case 1:
                print(1)
            case 2:
                print(2)
            case 3:
                print(3)
            case 4:
                print(4)
                break
    return

def make_attack(targets, aircrafts, pilots):
    result = []
    for target in targets:
        for pilot in pilots:
            for aircraft in aircrafts:
                new_attack = Attack(aircraft, pilot, target)
                result.append(new_attack)

    return result
# create targets instance
all_targets = [Targets(x['City'], *read_location(x['City']), x['Priority']) for x in read_json('filses/targets.json')]
all_aircraft = [Aircraft(x['type'], x['speed'], x['fuel_capacity']) for x in read_json('filses/aircrafts.json')]
all_pilots = [Pilot(x['name'], x['skill_level']) for x in read_json('filses/pilots.json')]
all_attack: list[Attack] = make_attack(all_targets, all_aircraft, all_pilots)

if __name__ == '__main__':
    # main_menu()
    # print([[x.distance, x.city, x.weather, x.weather_rank] for x in all_targets])
    # for f in all_pilots:
    #     print(f)
    n = 0
    for i in all_attack:
        print(i.rank)
        n += 1
    print(n)
    print(all_attack[0])
    print(all_attack[10])
    print(all_attack[1000])
    print(len(all_attack))



