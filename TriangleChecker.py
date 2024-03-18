import math

class TriangleChecker:
    def getPointCoordinates(self, point_name):
        # Get valid integer coordinates for a point from the user
        while True:
            try:
                x, y = map(int, input(f"Enter coordinates of point {point_name} (x y): ").split())
                if x < 0 or y < 0:
                    print("Coordinates must be positive integers.")
                    continue
                return x, y
            except ValueError:
                print("Invalid input. Please enter valid integer coordinates (x y).")

    def calcDistance(self, x1, y1, x2, y2):
        # Calculate the distance between two points using the distance formula
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def checkTriangleValidity(self, side_lengths):
        # Check if the given side lengths form a valid triangle using the triangle inequality theorem
        a, b, c = sorted(side_lengths)
        return a + b > c

    def checkTriangle(self, x1, y1, x2, y2, x3, y3):
        # Check if the given points form a valid triangle
        side_lengths = [
            self.calcDistance(x1, y1, x2, y2),
            self.calcDistance(x2, y2, x3, y3),
            self.calcDistance(x1, y1, x3, y3)
        ]
        return self.checkTriangleValidity(side_lengths)

    def run(self):
        while True:
            choice = input("Enter coordinates of three points or type 'exit' to quit: ")
            if choice.lower() == "exit":
                print("Exiting the program.")
                break
            try:
                x1, y1 = self.getPointCoordinates("A")
                x2, y2 = self.getPointCoordinates("B")
                x3, y3 = self.getPointCoordinates("C")
                is_triangle = self.checkTriangle(x1, y1, x2, y2, x3, y3)
                if is_triangle:
                    print("The points form a valid triangle.")
                else:
                    print("The points do not form a valid triangle.")
            except Exception as e:
                print("An error occurred:", str(e))

if __name__ == "__main__":
    checker = TriangleChecker()
    checker.run()
