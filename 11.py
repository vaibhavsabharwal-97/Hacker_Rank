if __name__ == '__main__':
    # Input for English newspaper subscribers
    n1 = int(input())
    english_subscribers = set(map(int, input().split()))

    # Input for French newspaper subscribers
    n2 = int(input())
    french_subscribers = set(map(int, input().split()))

    # Calculate the difference (subscribers only in English) and print the total
    english_only_subscribers = english_subscribers.difference(french_subscribers)
    total_english_only_subscribers = len(english_only_subscribers)

    print(total_english_only_subscribers)
