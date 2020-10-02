class Rectangle:

    def __init__(self, h = 0, w = 0):
        self.height = w
        self.width = h

    def __str__(self):
        return ("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")")

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return (self.height * self.width)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (( self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):

        arr = ""

        if (self.width >= 50 or self.height >= 50) :
            return ("Too big for picture.")
        for i in range(self.height):
            arr += "*" * self.width + "\n"
        return (arr)
    
    def get_amount_inside(self, other):
        return (self.height // other.height) * (self.width // other.width)

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
        super().__init__(self.height, self.width)
    
    def __str__(self):
        return ("Square(side=" + str(self.height) + ")")

    def set_side(self, side):
        self.width = side
        self.height = side
    
def main():

    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(3)
    print(rect.get_perimeter())
    print(rect)

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)


if __name__ == "__main__":
    main()