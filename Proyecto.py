def run():
    my_list = [1, 2, 3, 4, 5]

    my_dict = {'uno': 1, 'dos': 2,'tres': 3}

    for name, value  in my_dict.items():
        print(name, " ", value)

if __name__ == '__main__':
    run()