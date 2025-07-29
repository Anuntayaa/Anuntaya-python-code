num = []
odd = []
even = []

while True:
    try:
        x1 = int(input('How many numbers do youwent to enter:'))
        if x1 <= 0:
            print('Numbre must be more than 0.')
            continue

        for i in range(1,x1+1):
            while True:
                try:
                    number = int(input(f'Number {1}:'))
                    if number < 0:
                        print('Number must be more than 0.')
                        continue
                    break
                except ValueError:
                    print('Please enter a valid number.')
                    continue

            num.append(number)
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)

        total = sum(num)
        average = total / len(num)
        minimum = min(num)
        maximum = max(num)

        gerater_than_avg = []
        for n in num:
            if n > average:
                gerater_than_avg.append(n)

        print("\n--- Results ---")
        print(f"Total number: {num}")
        print(f"Even number: {even}")
        print(f"Odd number: {odd}")
        print(f"Numbers greater than avreage: {gerater_than_avg}")
        print(f"Sum: {total}")
        print(f"Average: {average}")
        print(f"min: {minimum}")
        print(f"Max: {maximum}")
        break
    
    except ValueError:
        print('Please enter a number.')
        continue