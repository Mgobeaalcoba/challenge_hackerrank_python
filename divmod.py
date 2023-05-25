# Enter your code here. Read input from STDIN. Print output to STDOUT
def run():
    dividendo = int(input())
    divisor = int(input())
    print(dividendo//divisor)
    print(dividendo%divisor)
    print(divmod(dividendo,divisor))

if __name__ == '__main__':
    run()