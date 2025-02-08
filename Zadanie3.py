def solve():
    line_num = 0
    while True:
        line = input()
        numbers = line.split('#')

        if '999' in numbers:
            numbers = numbers[:numbers.index('999')]

        if not numbers:
            break

        first_num = numbers[0]
        forbidden_digits = set(first_num)

        valid_numbers = []
        for num_str in numbers[1:]:
            valid = True
            for digit in num_str:
                if digit in forbidden_digits:
                    valid = False
                    break
            if valid:
                valid_numbers.append(int(num_str))

        valid_numbers = sorted(list(set(valid_numbers)))

        if valid_numbers:
            print(*valid_numbers, end="")
            if line_num % 2 == 0:
                print(" {}".format(sum(valid_numbers)))
            else:
                print()
        else:
            print()

        line_num += 1

solve()


