class Fraction:

    def __init__(self, top, bottom):
        try:
            top = int (top)
            bottom = int (bottom)
            common = Fraction.gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common
        except ValueError:
            raise RuntimeError("Only integers allowed in fractions")

    def show(self):
        print(Fraction.__str__(self))

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

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
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        return Fraction.__add__(self, other)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __sub__(self, other):
        new_num = self.num*other.den - \
            self.den*other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        return self * Fraction(other.den, other.num)

    def __repr__(self):
        return 'Fraction (' + str(self.num) + ',' + str(self.den) + ')'

customFraction = Fraction(4,8)
customFraction.show()

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
print("Numerator of F1 is %d" % f1.get_num())
print("Denominator of F1 is %d" % f1.get_den())

q1 = Fraction(1,4) + Fraction(1,4)
print(q1)

q1 = Fraction(3,4) + Fraction(1,6)
print(q1)

q1 = Fraction(3,4) - Fraction(1,6)
print(q1)

q1 = Fraction(1,2) - Fraction(1,6)
print(q1)

q1 = Fraction(2,3) * Fraction(11,5)
print(q1)

q1 = Fraction(1,2) / Fraction(1,6)
print(q1)

q1 = Fraction(1,8) / Fraction(1,4)
print(q1)

q1 = Fraction(2,3) / Fraction(11,5)
print(q1)

print(repr(q1))