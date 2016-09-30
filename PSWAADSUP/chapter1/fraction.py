class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(Fraction.__str__(self))

    def __str__(self):
        return "%d/%d" % (self.num, self.den)

    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def __add__(self, other):
        new_num = self.num*other.den + \
            self.den*other.num
        new_den = self.den * other.den
        common = Fraction.gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

myFraction = Fraction(3,5)
myFraction.show()
print("I ate", myFraction, "of the pizza")
print(myFraction.__str__())
print(str(myFraction))

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print(f3)
print(Fraction.__eq__(f1,Fraction(1,4)))