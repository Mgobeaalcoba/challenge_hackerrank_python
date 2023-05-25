def run():
    n = int(input("Ingrese la cantidad de valores: "))
    arr = map(int, input("Ingrese un valor: ").split())

    my_list = list(arr)
    print(n)
    print(arr)
    print(my_list)

    my_list.sort(reverse=True)

    my_max = max(my_list)

    print(my_list)

    print(my_max)

    while my_max in my_list:
        my_list.remove(my_max)

    my_second_max = my_list[0]

    print(my_second_max)

if __name__ == '__main__':
    run()