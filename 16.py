if __name__ == '__main__':
    # Read the elements of the main set A
    set_A = set(map(int, input().split()))

    # Read the number of other sets
    num_sets = int(input())

    is_strict_superset = True

    # Process each set and check if set A is a strict superset
    for _ in range(num_sets):
        set_B = set(map(int, input().split()))

        # Check if set A is not a strict superset of set B
        if not set_B.issubset(set_A) or set_A == set_B:
            is_strict_superset = False
            break

    # Print the result
    print(is_strict_superset)
