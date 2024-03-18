import logging
import math

class ElectricityCalculator:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)  # Set logging level as needed
        self.logger = logging.getLogger(__name__)

    def calcElectricityCharges(self, units):
        if units <= 0:
            return "Invalid Input", ""

        totalAmt = 0
        breakdown = []

        try:
            # Calculate electricity charges based on units consumed and slab rates
            if units <= 100:
                amount = units * 0.0
                totalAmt += amount
                breakdown.append((1, units, 0.0, amount))
            elif units <= 200:
                amount = 100 * 0.0 + (units - 100) * 1.5
                totalAmt += amount
                breakdown.append((1, 100, 0.0, 100 * 0.0))
                breakdown.append((101, units, 1.5, (units - 100) * 1.5))
            elif units <= 500:
                amount = 100 * 0.0 + 100 * 2 + (units - 200) * 3.0
                totalAmt += amount
                breakdown.append((1, 100, 0.0, 100 * 0.0))
                breakdown.append((101, 200, 2, 100 * 2))
                breakdown.append((201, units, 3.0, (units - 200) * 3.0))
            else:
                amount = 100 * 0.0 + 100 * 3.5 + 300 * 4.6 + (units - 500) * 6.6
                totalAmt += amount
                breakdown.append((1, 100, 0.0, 100 * 0.0))
                breakdown.append((101, 200, 3.5, 100 * 3.5))
                breakdown.append((201, 500, 4.6, 300 * 4.6))
                breakdown.append((501, units, 6.6, (units - 500) * 6.6))

            return totalAmt, breakdown
        except Exception as e:
            # Handle any exceptions that occur during calculation
            return "Error occurred:", str(e)

    def run(self):
        while True:
            try:
                # Get input for units consumed
                input_str = input("Please enter the number of units consumed (type 'exit' to quit): ")
                if input_str.lower() == 'exit':
                    print("Exiting the program...")
                    break

                unitsConsumed = int(input_str)

                # Calculate electricity charges and get breakdown
                totalAmt, breakdown = self.calcElectricityCharges(unitsConsumed)

                if isinstance(totalAmt, float):
                    # Print breakdown and total amount if calculation is successful
                    logging.info(f"For {unitsConsumed} units consumed, the bill amount breakdown is as follows:")
                    for slab in breakdown:
                        logging.info(f"Units from {slab[0]} to {slab[1]} at rate Rs. {slab[2]} per unit: Rs. {slab[3]:.2f}")
                    logging.info(f"Total amount to be paid for {unitsConsumed} units is: Rs. {totalAmt:.2f}")
                else:
                    # Print error message if calculation failed
                    logging.error(totalAmt)
            except ValueError:
                # Handle invalid input error
                logging.error("Invalid input. Please enter a valid number of units.")
            except Exception as ex:
                # Handle other exceptions
                logging.exception("An error occurred:")

if __name__ == "__main__":
    # Create an instance of ElectricityCalculator class and run the program
    calculator = ElectricityCalculator()
    calculator.run()
