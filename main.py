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


if __name__ == '__main__':
    main_menu()