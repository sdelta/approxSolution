import unittest
import compileexpr

def approxEqual(a, b, eps=0.00000001):
    if abs(a-b) < eps:
        return True
    else:
        return False

class TestCompileExpr(unittest.TestCase):
    def test_integerConstants(self):
        self.assertEqual(compileexpr.calculate("1"), 1)
        self.assertEqual(compileexpr.calculate("12345"), 12345)


    def test_notIntegerConstants(self):
        self.assertTrue(approxEqual(compileexpr.calculate("1.0"), 1.0))
        self.assertTrue(approxEqual(compileexpr.calculate("12.345"), 12.345))
        self.assertTrue(approxEqual(compileexpr.calculate("0.123"), 0.123))

    def test_simpleCalculations(self):
        self.assertEqual(compileexpr.calculate("3+2"), 5)
        self.assertEqual(compileexpr.calculate("3-2"), 1)
        self.assertEqual(compileexpr.calculate("3*2"), 6)
        self.assertTrue(approxEqual(compileexpr.calculate("6/2"), 3.0))

    def test_operationOrder(self):
        self.assertEqual(compileexpr.calculate("2+3*4"), 14)
        self.assertEqual(compileexpr.calculate("3*4+2"), 14)

        self.assertEqual(compileexpr.calculate("2-3*4"), -10)
        self.assertEqual(compileexpr.calculate("3*4-2"), 10)

        self.assertTrue(approxEqual(compileexpr.calculate("2+12/3"), 6.0))
        self.assertTrue(approxEqual(compileexpr.calculate("12/3+2"), 6.0))

        self.assertTrue(approxEqual(compileexpr.calculate("2-12/3"), -2.0))
        self.assertTrue(approxEqual(compileexpr.calculate("12/3-2"), 2.0))

    def test_expressionsWithBrackets(self):
        self.assertEqual(compileexpr.calculate("2*(3+4)"), 14)
        self.assertEqual(compileexpr.calculate("(3+4)*2"), 14)

        self.assertEqual(compileexpr.calculate("5*(2+3*4)"), 70)
        self.assertEqual(compileexpr.calculate("5*(3*4+2)"), 70)
        self.assertEqual(compileexpr.calculate("(2+3*4)*5"), 70)
        self.assertEqual(compileexpr.calculate("(3*4+2)*5"), 70)

    def test_unaryMinus(self):
        self.assertEqual(compileexpr.calculate("-1"), -1)
        self.assertTrue(approxEqual(compileexpr.calculate("-0.123"), -0.123))

        self.assertEqual(compileexpr.calculate("-1*-1"), 1)
        self.assertEqual(compileexpr.calculate("-6*-(-2+3*4)"), 60)

if __name__ == "__main__":
    unittest.main()