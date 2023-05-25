def run():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg_notes = sum(student_marks[query_name])/len(student_marks[query_name])
    formatted_number = "{:.2f}".format(avg_notes)
    print(formatted_number)

if __name__ == '__main__':
    run()

