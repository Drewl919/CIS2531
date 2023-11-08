class Rational(object):
    """This creates a rational number (fraction)"""
    def __init__(self, numerator=0, denominator=1):
        """Constructor for a rational number with a numerator and denominator"""
        self.__originalNumerator = numerator
        self.__originalDenominator = denominator
        self.__reducedNumerator = numerator
        self.__reducedDenominator = denominator
        self.reduce()
        self.__numerator = numerator
        self.__denominator = denominator

    def getNumerator(self):
        """gets and returns the first value of the complex number"""
        return self.__numerator
    def getDenominator(self):
        """gets and returns the second value of the complex number"""
        return self.__denominator

    def getOriginal(self):
        """returns a string representation of the original rational number"""
        return f"{self.__originalNumerator}/{self.__originalDenominator}"

    def getDecimal(self):
        """returns a string representatin of the rational number in decimal form"""
        dec = str(self.__originalNumerator/self.__originalDenominator)
        return dec

    def reduce(self):
        """reduces the rational number """
        gcf = self.__getGCF(self.__originalNumerator, self.__originalDenominator)
        self.__reducedNumerator = int(self.__reducedNumerator/gcf)
        self.__reducedDenominator = int(self.__reducedDenominator/gcf)

    def getRational(self):
        """return a string representation of the reduced rational number"""
        return f"{self.__reducedNumerator}/{self.__reducedDenominator}"

    def displayData(self):
        print()
        print(self.getOriginal() + " equals "+ self.getDecimal() +" and ")
        print(self.getOriginal() + " reduces to "+ self.getRational())
        print()

    @staticmethod
    def multiply(r1, r2):
        """multiplies r1 by r2 and returns the result as a complex number"""
        numerator = r1.getNumerator() * r2.getNumerator()
        denominator = r1.getDenominator() * r2.getDenominator()
        return Rational(numerator, denominator)

    @staticmethod
    def divide(r1, r2):
        """divides r1 by r2 and returns the result as a complex number"""
        numerator = r1.getNumerator() * r2.getDenominator()
        denominator = r1.getDenominator() * r2.getNumerator()
        return Rational(numerator, denominator)

    @staticmethod
    def add(r1, r2):
        """adds r1 with r2 and returns the result as a complex number"""
        numerator = (r1.getNumerator()*r2.getDenominator()) + (r2.getNumerator()*r1.getDenominator())
        denominator = r1.getDenominator() * r2.getDenominator()
        return Rational(numerator, denominator)

    @staticmethod
    def subtract(r1, r2):
        """subtracts r2 from r1 and returns the result as a complex number"""
        numerator = (r1.getNumerator() * r2.getDenominator()) - (r2.getNumerator() * r1.getDenominator())
        denominator = r1.getDenominator() * r2.getDenominator()
        return Rational(numerator, denominator)

    def __getGCF(self,num1:int, num2:int):
        """returns the greatest common factor of 2 integer values"""
        rem = None
        gcf = None
        while (rem != 0):
            rem = num1 % num2
            if (rem == 0):
                gcf = num2
            else:
                num1 = num2
                num2 = rem
        return gcf

class ComplexNumber(object):
    def __init__(self, a, b):
        """Constructor for a rational number with a numerator and denominator"""
        self.realPart = a
        self.complexPart = b
