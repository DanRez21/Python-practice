import factorial.factorial
import logarithm.logarithm
import exp_root.exponentiation
import exp_root.root

def check(n, type):
    try:
        n = type(n)
        return True
    except ValueError:
        return False
        
def main():
    num = input("Please, choose function:\n1.Find x²\n2.Find x³\n3.Find √x\n4.Find ∛x\n5.Find factorial x!\n6.Find log()\n7.Find ln()\n8.Find lg()\nYour number: ")
    if num == '1':
        n = input("Please, input x: ")
        if check(n, float):
            print("x² = ", round(exp_root.exponentiation.exp2(float(n)), 4))
        else:
            print("Must be a number, not symbols")
    elif num == '2':
        n = input("Please, input x: ")
        if check(n, float):
            print("x³ = ", round(exp_root.exponentiation.exp3(float(n)), 4))
        else:
            print("Must be a number, not symbols")
    elif num == '3':
        n = input("Please, input x: ")
        if check(n, float) and float(n) >= 0:
            print("√x = ", round(exp_root.root.root2(float(n)), 4))
        else:
            print("Must be a number that is greater than zero")
    elif num == '4':
        n = input("Please, input x: ")
        if check(n, float):
            print("∛x = ", round(exp_root.root.root3(float(n)),4))
        else:
            print("Must be a number, not symbols")
    elif num == '5':
        n = input("Please, input x: ")
        if check(n, int) and int(n) > 0:
            print("x! = ", factorial.factorial.fact(int(n)))
        else:
            print("Must be a number that is greater than zero")
    elif num == '6':
        a = input("Please, input base of logarithm: ")
        b = input("Please, input x: ")
        if check(a, float) and check(b, float) and float(b) > 0 and float(a) > 0 and float(a) != 1:
            print("log(base)(x) = ", round(logarithm.logarithm.logf(float(b), float(a)), 4))
        else:
            print("Must be a numbers that is greater than zero")
    elif num == '7':
        b = input("Please, input x: ")
        if check(b, float) and float(b) > 0:
            print("ln(x) = ", round(logarithm.logarithm.ln(float(b)), 4))
        else:
            print("Must be a number that is greater than zero")
    elif num == '8':
        b = input("Please, input x: ")
        if check(b, float) and float(b) > 0:
            print("lg(x) = ", round(logarithm.logarithm.log10(float(b)), 4))
        else:
            print("Must be a number that is greater than zero")
    else:
        print("Not correctly number of function")

if __name__ == '__main__':
    main()