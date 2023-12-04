if __name__ == '__main__':
    # Input for English newspaper subscribers
    n1 = int(input())
    english_subscribers = set(map(int, input().split()))

    # Input for French newspaper subscribers
    n2 = int(input())
    french_subscribers = set(map(int, input().split()))

    # Calculate the symmetric difference and print the total
    symmetric_difference_subscribers = english_subscribers.symmetric_difference(french_subscribers)
    total_symmetric_difference_subscribers = len(symmetric_difference_subscribers)

    print(total_symmetric_difference_subscribers)
