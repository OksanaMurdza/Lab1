import dblogic
import datetime

while True:
    print('')
    print('Select table:')
    print('1. cinemas')
    print('2. seances')
    print('e. Exit program')
    menu_input_table = raw_input()

    if menu_input_table == '1':
        while True:
            print('')
            print('Select action for table \'cinemas\':')
            print('1. Create')
            print('2. Update')
            print('3. Delete')
            print('4. Select')
            print('e. Go back')
            menu_input_table_cinemas = raw_input()

            if menu_input_table_cinemas == '1':
                try:
                    print('')
                    print('Enter cinema name:')
                    cinema_name = str(raw_input())
                    print('Enter cinema address:')
                    cinema_address = str(raw_input())

                    dblogic.create_cinema(cinema_name, cinema_address)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_cinemas == '2':
                try:
                    print('')
                    print('Enter id name that you want to update')
                    cinema_id = input()

                    if (dblogic.select_cinema('id', id)) == 0:
                        raise Exception('Error: there is no cinema with id \'{0}\''.format(id))

                    print('')
                    print('Enter field that you want to update (\'name\', \'address\')')
                    update_field = raw_input()
                    if (update_field != 'name') and (update_field != 'address'):
                        raise Exception('Error: invalid field')

                    print('')
                    print('Enter value:')
                    update_value = raw_input()

                    dblogic.update_cinema(cinema_id, update_field, update_value)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_cinemas == '3':
                try:
                    print('')
                    print('Enter cinema id that you want to delete')
                    cinema_name = input()

                    if(dblogic.select_cinema('id', id)) == 0:
                        raise Exception('Error: there is no cinema with name \'{0}\''.format(cinema_name))

                    dblogic.delete_cinema(cinema_name)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_cinemas == '4':
                try:
                    print('')
                    print('Enter field that you want to filter (\'name\', \'address\'), or leave blank to list all')
                    input_field = raw_input()
                    if (input_field != 'name') and (input_field != 'address') and (input_field != ''):
                        raise Exception('Error: invalid field')

                    if input_field == '':
                        print('')
                        dblogic.print_cinemas(dblogic.select_cinema())
                        continue

                    print('')
                    print('Enter \'{0}\' value:'.format(input_field))
                    input_value = raw_input()
                    print('')
                    dblogic.print_cinemas(dblogic.select_cinema(input_field, input_value))
                except Exception as e:
                    print('')
                    print(e)

            elif menu_input_table_cinemas == 'e':
                break

    elif menu_input_table == '2':
        while True:
            print('')
            print('Select action for table \'seances\':')
            print('1. Create')
            print('2. Update')
            print('3. Delete')
            print('4. Select')
            print('5. Filter')
            print('e. Go back')
            menu_input_table_seances = raw_input()

            if menu_input_table_seances == '1':
                try:
                    print('')
                    print('Type seances \'cinema_name\', \'price\' separated by spaces:')
                    input_seance = raw_input().split(' ')

                    print 'Enter date (yyyy mm dd h m)'
                    yy, mm, dd, h, m = map(int, str(raw_input()).split())
                    myDateTime = datetime.datetime(yy, mm, dd, h, m)

                    if len(input_seance) < 2:
                        raise Exception('Error: you must provide three arguments')
                    dblogic.create_seance(input_seance[0], myDateTime, input_seance[1])
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_seances == '2':
                try:
                    print('')
                    print('Enter id seance that you want to update')
                    up_id = input()

                    if (dblogic.select_seances('id', id)) == 0:
                        raise Exception('Error: there is no seance with price \'{0}\''.format(up_id))

                    print('')
                    print('Enter field that you want to update (\'date_time\', \'price\')')
                    update_field = raw_input()
                    if (update_field != 'date_time') and (update_field != 'price'):
                        raise Exception('Error: invalid field')

                    print('')
                    if update_field == 'date_time':
                        print 'Enter date (yyyy mm dd h m)'
                        yy, mm, dd, h, m = map(int, str(raw_input()).split())
                        update_value = datetime.datetime(yy, mm, dd, h, m)
                    else:
                        print('Enter value:')
                        update_value = input()

                    dblogic.update_seance(up_id, update_field, update_value)
                except Exception as e:
                    print('')
                    print(e)

            elif menu_input_table_seances == '3':
                try:
                    print('')
                    print('Enter id seance that you want to delete')
                    del_id = input()

                    if (dblogic.select_seances('id', id)) == 0:
                        raise Exception('Error: there is no seance \'{0}\''.format(del_id))

                    dblogic.delete_seance(del_id)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_seances == '4':
                try:
                    print('')
                    print('Enter field that you want to filter (\'cinema_name\', \'data_time\', \'price\'), '
                          'or leave blank to list all')
                    input_field = raw_input()
                    if (input_field != 'cinema_name') and (input_field != 'data_time') \
                            and (input_field != 'price') and (input_field != ''):
                        raise Exception('Error: invalid field')

                    if input_field == '':
                        print('')
                        dblogic.print_seances(dblogic.select_seances())
                        continue

                    print('')
                    print('Enter \'{0}\' value:'.format(input_field))
                    input_value = raw_input()
                    print('')
                    dblogic.print_seances(dblogic.select_seances()(input_field, input_value))
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_seances == '5':
                try:
                    print('')
                    print('Showing cinema, where seances after 18 hours:')
                    print('')
                    dblogic.print_seances(dblogic.filter_seances())
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_seances == 'e':
                break
    elif menu_input_table == 'e':
        exit(0)
