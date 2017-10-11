import database
import datetime

def select_cinema(key=None, value=None):
    if key == None:
        return db.data['cinemas']

    cinema_array = []

    for cinema in db.data['cinemas']:
        if cinema[key] == value:
            cinema_array.append(cinema)

    return cinema_array


def create_cinema(name, address):
    if len(select_cinema('name', name)) > 0:
        raise Exception('Error: cinema with name \'{0}\' already exists'.format(name))

    db.data['cinemas'].append({
        'id': db.data['config']['cid_current'],
        'name': name,
        'address': address,
    })

    db.data['config']['cid_current'] += 1


def update_cinema(id, key, value):
    for cinema in db.data['cinemas']:
        if cinema['id'] == id:
            cinema[key] = value
            break


def delete_cinema(id):
    for cinema in db.data['cinemas']:
        if cinema['id'] == id:
            for seance in db.data['seances']:
                if seance['cinema_name'] == cinema['name']:
                    db.data['seances'].remove(seance)
            db.data['cinemas'].remove(cinema)
            break


def print_cinemas(cinemas):
    for cinema in cinemas:
        print('[{0}] {1} {2}'.format(cinema['id'], cinema['name'], cinema['address']))


def select_seances(key=None, value=None):
    if not key:
        return db.data['seances']

    seance_array = []
    for seance in db.data['seances']:
        if seance[key] == value:
            seance_array.append(seance)

    return seance_array


def create_seance(cinema_name, date_time, price):
    if len(select_cinema('name', cinema_name)) == 0:
        raise Exception('Error: there is no cinema with name \'{0}\''.format(cinema_name))

    db.data['seances'].append({
        'id': db.data['config']['sid_current'],
        'cinema_name': cinema_name,
        'date_time': date_time,
        'price': price,
    })

    db.data['config']['sid_current'] += 1


def update_seance(id, key, value):
    for seance in db.data['seances']:
        if seance['id'] == id:
            seance[key] = value
            break


def delete_seance(id):
    for seance in db.data['seances']:
        if seance['id'] == id:
            db.data['seances'].remove(seance)
            break


def print_seances(seances):
    for seance in seances:
        print('[{0}] {1} {2} {3}'.format(seance['id'], seance['cinema_name'], seance['date_time'], seance['price']))


def filter_seances():
    seances_result = []

    for seance in db.data['seances']:
        if seance['date_time'].hour >= 18:
            seances_result.append(seance)
    return seances_result

db = database.database()

if db.data['config']['initMe']:
    create_cinema('Cinemacity', 'Antonovicha 176')
    create_cinema('Butterfly', 'Vadyma Hetmana 6')
    create_cinema('Kyiv', 'Velyka Vasylkivska 19')

    create_seance('Cinemacity', datetime.datetime(2017, 10, 02, 21, 00), 50)
    create_seance('Butterfly', datetime.datetime(2017, 10, 02, 17, 30), 40)
    create_seance('Kyiv', datetime.datetime(2017, 10, 02, 19, 30), 85)
    create_seance('Butterfly', datetime.datetime(2017, 10, 02, 15, 45), 55)
    create_seance('Kyiv', datetime.datetime(2017, 10, 02, 12, 30), 35)
    create_seance('Cinemacity', datetime.datetime(2017, 10, 02, 23, 20), 95)

    db.data['config']['initMe'] = False