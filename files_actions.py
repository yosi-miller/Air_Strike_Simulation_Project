from json import load


def read_json(path):
    """
    this function reads the json file
    :param path: the path of the json file
    :return:
    """
    with open(path, 'r') as json_file:
        return load(json_file)


if __name__ == '__main__':
    # t_info = read_json('filses/targets.json')
    # all_targets = [Targets(x['City'],2, 3, x['Priority']) for x in t_info]
    # print([x.distance for x in all_targets])
    # print(t_info)
    f_info = read_json('filses/aircrafts.json')
    print(f_info)