if __name__ == '__main__':
    # Input for English newspaper subscribers
    n1 = int(input())
    english_subscribers = set(map(int, input().split()))

    # Input for French newspaper subscribers
    n2 = int(input())
    french_subscribers = set(map(int, input().split()))

    # Calculate the intersection (common subscribers) and print the total
    common_subscribers = english_subscribers.intersection(french_subscribers)
    total_common_subscribers = len(common_subscribers)

    print(total_common_subscribers)
