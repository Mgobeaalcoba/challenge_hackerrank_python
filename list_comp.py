def run():
    x = int(input("Ingrese un numero x: "))
    y = int(input("Ingrese un numero y: "))
    z = int(input("Ingrese un numero z: "))
    n = int(input("Ingrese un numero n: "))
    
    my_list = []
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                my_list.append([i,j,k])

    my_list_2 = my_list.copy()

    print(my_list)
    print(f"len of my list: {len(my_list)}")
    print()
    
    for list in my_list:
        print(f"sum(list): {sum(list)}")
        print(f"n: {n}")
        if sum(list) == n:
            if list in my_list_2:
                print("Es igual... Remuevo")
                my_list_2.remove(list)

    print(my_list_2)
    print(f"len of my list: {len(my_list_2)}")
    print()

if __name__ == '__main__':
    run()