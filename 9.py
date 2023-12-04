if __name__ == '__main__':
    n = int(input())  # Number of students' records
    student_records = {}  # Dictionary to store name:[marks]

    # Reading the names and marks for each student
    for _ in range(n):
        record = input().split()
        name, marks = record[0], list(map(float, record[1:]))
        student_records[name] = marks

    query_name = input()  # Name of the student to query

    # Calculating and printing the average marks for the queried student
    average_marks = sum(student_records[query_name]) / len(student_records[query_name])
    print("{:.2f}".format(average_marks))
