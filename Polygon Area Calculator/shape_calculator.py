class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h
    def set_width(self,w):
        self.width=w
    def set_height(self,h):
        self.height=h
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width+2*self.height
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.height <= 50:
            if self.width <= 50:
                h=''
                for i in range(self.height):
                    for j in range(self.width):
                        S='*'
                        h=h+S
                    h=h+'\n'
                return h
            else:
                return "Too big for picture."
        else:
            return "Too big for picture."
    def get_amount_inside(self,shape):
        width=shape.width
        height=shape.height
        div1=self.width//width
        div2=self.height//height
        return div1*div2
    def __str__(self):
        if self.width != self.height:
            return f"Rectangle(width={self.width}, height={self.height})"
        else:
            return f"Square(side={self.width})"
class Square(Rectangle):
    def __init__(self,side):
        self.width=side
        self.height=side
    def set_side(self,side):
        self.width=side
        self.height=side
    def set_width(self,w):
        self.width=w
        self.height=w
if __name__ == "__main__":
   sq= Square(4)
   print(sq.get_area())
