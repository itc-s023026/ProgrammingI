class Square(Rectangle):
    def __int__(self, width):
        super().__int__(width, width)
        self.name = "square"


s1 = Square(4)
s1.show_attributes()
