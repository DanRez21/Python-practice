import factorial.factorial
import logarithm.logarithm
import exp_root.exponentiation
import exp_root.root


def check(n, type):
    try:
        n = type(n)
        return True
    except Exception:
        return False
        
def main():
    num = input("Please, choose function:\n1.root x²\n2.root x³\n3.root √x\n4.root ∛x\n5.factorial x!\n6.log()\n7.ln()\n8.lg()\nYour number: ")
    if num == '1':
        n = input("Please, input x: ")
        if check(n, float):
            n = float(n)
            print("x² = ", round(exp_root.exponentiation.exp2(n), 4))
        else:
            print("You make a mistake")
    elif num == '2':
        n = input("Please, input x: ")
        if check(n, float):
            n = float(n)
            print("x³ = ", round(exp_root.exponentiation.exp3(n), 4))
        else:
            print("You make a mistake")
    elif num == '3':
        n = input("Please, input x: ")
        if check(n, float) and float(n) >= 0:
            n = float(n)
            print("√x = ", round(exp_root.root.root2(n), 4))
        else:
            print("You make a mistake")
    elif num == '4':
        n = input("Please, input x: ")
        if check(n, float):
            n = float(n)
            print("∛x = ", exp_root.root.root3(n))
        else:
            print("You make a mistake")
    elif num == '5':
        n = input("Please, input x: ")
        if check(n, int) and int(n) > 0:
            n = int(n)
            print("x! = ", factorial.factorial.fact(n))
        else:
            print("You make a mistake")
    elif num == '6':
        a = input("Input base of logarithm: ")
        b = input("Input x: ")
        if check(a, float) and check(b, float) and float(b) > 0 and float(a) > 0 and float(a) != 1:
            a, b = float(a), float(b)
            print("log(base)(x) = ", round(logarithm.logarithm.logf(b, a), 4))
        else:
            print("You make a mistake")
    elif num == '7':
        b = input("Input x: ")
        if check(b, float) and float(b) > 0:
            b = float(b)
            print("ln(x) = ", round(logarithm.logarithm.ln(b), 4))
        else:
            print("You make a mistake")
    elif num == '8':
        b = input("Input x: ")
        if check(b, float) and float(b) > 0:
            b = float(b)
            print("lg(x) = ", round(logarithm.logarithm.log10(b), 4))
        else:
            print("You make a mistake")
    else:
        print("Not correctly number of function")

if __name__ == '__main__':
    main()