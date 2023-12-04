def is_subset(A, B):
    return A.issubset(B)

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())

    # Process each test case
    for _ in range(t):
        # Read the elements of set A
        _ = input()  # Ignore the size of set A as it's not needed
        set_A = set(map(int, input().split()))

        # Read the elements of set B
        _ = input()  # Ignore the size of set B as it's not needed
        set_B = set(map(int, input().split()))

        # Check if set A is a subset of set B and print the result
        result = is_subset(set_A, set_B)
        print(result)
