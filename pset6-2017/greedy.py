import cs50

# This program requests input from the user on how much change is owed.
# It then calculates the minimum number of coins required to provide the change.
    
def main():
    while True:
        print("How much change do I owe you?")
        change = cs50.get_float()
        if change>0:
            break
    
    # Converts the amount of change into dollars and round to the nearest
    # whole integer. Doing this will prevent errors from imprecise decimals
    # in float values.
    cents = round(change * 100)
    
    q = 25
    d = 10
    n = 5
    p = 1
    
    # Start with the coin of largest value (quarter = q) and work your way down
    # to the smallest value (penny = p).
    count = cents // q
    cents = cents % q
    count += cents // d
    cents = cents % d
    count += cents // n
    cents = cents % n
    count += cents // p
    cents = cents % p
    print(count)

if __name__ == "__main__":
    main()
