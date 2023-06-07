# __main__.py
import foo
import bar

def get_total(x, y):
    return x + y 

def main():
    x = foo.foo()
    y = bar.bar()
    total = get_total(x, y)
    print(f"{x} + {y} = {total}")
    return

if __name__ == "__main__":
    main()

