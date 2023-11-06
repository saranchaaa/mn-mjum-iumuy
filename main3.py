import colorama as c

def e(num1):
    i = 0
    p = input("Number? - ")

    while True:
        print(c.Fore.GREEN)

        result = num1 ** i
        yield result

        if p in str(result):
            return

        i += 1


x = e(2)
for l in x:
    print(l)
