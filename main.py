from models.aircraft import Aircraft
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

# create targets instance
# all_targets = [Targets(x['City'], *read_location(x['City']), x['Priority']) for x in read_json('filses/targets.json')]
all_aircraft = [Aircraft(x['type'], x['speed'], x['fuel_capacity']) for x in read_json('filses/aircrafts.json')]
all_pilots = [Pilot(x['name'], x['skill_level']) for x in read_json('filses/pilots.json')]

if __name__ == '__main__':
    # main_menu()
    # print([[x.distance, x.city, x.weather, x.weather_rank] for x in all_targets])
    for f in  all_pilots:
        print(f)