if __name__ == '__main__':
    # Input for the initial set
    n = int(input())
    initial_set = set(map(int, input().split()))

    # Input for the number of other sets
    num_operations = int(input())

    # Perform the mutation operations
    for _ in range(num_operations):
        operation_info = input().split()
        operation_name = operation_info[0]
        other_set_size = int(operation_info[1])
        other_set = set(map(int, input().split()))

        # Perform the specified operation on the initial set
        if operation_name == 'intersection_update':
            initial_set.intersection_update(other_set)
        elif operation_name == 'update':
            initial_set.update(other_set)
        elif operation_name == 'symmetric_difference_update':
            initial_set.symmetric_difference_update(other_set)
        elif operation_name == 'difference_update':
            initial_set.difference_update(other_set)

    # Print the sum of elements in the final set
    print(sum(initial_set))
