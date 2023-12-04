# The Captain's Room
if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))

    # From the sample output, each number appears k times, except the captains room no
    room_set = set(rooms)  # unique room numbers

    # sum(room_set) * 5 --> Returns the sum of room numbers considering all room apper k times (including captain's room)
    # sum(rooms) --> Sum of all room numbers where the captains room appear only once
    # Captains room no --> (Sum (where captains room appear k times) - sum(rooms)) / (k - 1)
    print((sum(room_set) * k - sum(rooms)) // (k - 1))
