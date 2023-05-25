def run():
    my_list: list = []

    for _ in range(int(input())):
        name: str = input()
        score: float = float(input())
        my_sub_list: list = [name, score]
        my_list.append(my_sub_list)

    print(f"my list: {my_list}")

    sorted_list: list = sorted(my_list, key= lambda x: (x[1], x[0]))

    sorted_list_copy: list = sorted_list.copy()

    print(f"sorted list: {sorted_list}")

    lowest: int = sorted_list[0][1]

    print(f"lowest: {lowest}")

    for pair in sorted_list: 
        if pair[1] == lowest:
            sorted_list_copy.remove(pair)

    print(f"sorted list copy without lowest: {sorted_list_copy}")

    second_lowest: int = sorted_list_copy[0][1]

    print(f"second lowest: {second_lowest}")

    for pair in sorted_list_copy: 
        if pair[1] == second_lowest:
            print(pair[0])
        else:
            continue


if __name__ == '__main__':
    run()