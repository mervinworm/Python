#Hare un cambio en la rama Python y quiero ver como se ve en mi usuario de MacOS

def run():
    my_list = [1, 2, 3, 4, 5]

    my_dict = {'uno': 1, 'dos': 2,'tres': 3}
    
    for name, value  in my_dict.items():
        print(name, " ", value)

    for i in my_list:
        print(i)

if __name__ == '__main__':
    run()