#HQuiero ver este cambio hecho desde mi MacOS hasta mi PC Windows

def run():
    my_list = [1, 2, 3, 4, 5]

    my_dict = {'uno': 1, 'dos': 2,'tres': 3}
    
    for name, value  in my_dict.items():
        print(name, " ", value)

    for i in my_list:
        print(i)

if __name__ == '__main__':
    run()