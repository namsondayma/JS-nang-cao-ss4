def check_base_5(string):
        if len(string)>18:
            return "NO"
        
        total = sum(int(digit)for digit in string if digit.isdigit())

        if total == 5:
            return"YES"
        else:
             return"NO"
        T = int(input())
        
        for _ in range(T):
            sequence = input()
            print(check_base_5(sequence))