class Rectangle:
    """This is a rectangle class...."""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle[x=1{self.x}, y={self.y}, width={self.width}, height={self.height}]"

    def contains(self, x, y):
        pass

    
def main():
    rect = Rectangle(0,0,10,20)
    print(rect)


if __name__ == "__main__":
    main()
