class AmicableNumbersChecker:
    def __init__(self):
        pass

    def findDivisorsSum(self, num):
        # Calculate sum of divisors of a number (excluding the number itself)
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum

    def checkAmicableNum(self, m, n):
        # Check if the given numbers are amicable
        if m <= 0 or n <= 0:
            return "Invalid input: Numbers should be positive integers."

        sum_M = self.findDivisorsSum(m)
        sum_N = self.findDivisorsSum(n)

        if sum_M == n and sum_N == m:
            return f"{m} and {n} numbers are Amicable"
        else:
            return f"{m} and {n} numbers are Not Amicable"

    def run(self):
        print("Enter two numbers separated by space (M N), or type 'exit' to quit:")
        while True:
            try:
                user_input = input(">> ")
                if user_input.lower() == 'exit':
                    break
                
                m, n = map(int, user_input.split())
                result = self.checkAmicableNum(m, n)
                print(result)
            except ValueError:
                print("Invalid input: Please enter two integers separated by space (M N).")
            except Exception as e:
                print("An error occurred:", str(e))


if __name__ == "__main__":
    # Create an instance of AmicableNumbersChecker class and run the program
    checker = AmicableNumbersChecker()
    checker.run()
