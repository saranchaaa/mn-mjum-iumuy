import colorama as c

def helper(work):
    iim = work

    def helper(work):
        return c.Fore.YELLOW + f"🐌 can {iim}, and then 🐌 will {work}"
    return helper


helper = helper("eat")
print(helper("drink."))
print(helper("not do anything."))
