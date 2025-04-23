# chunk_gen.py

def gen_ints(n):
    for i in range(n):
        yield i

def gen_chunk(gen, size):
    for _ in range(size):
        try:
            yield next(gen)
        except StopIteration:
            return

def print_with_gen(n, size=5):
    gen = gen_ints(n)
    last_chunk = []
    while True:
        chunk = list(gen_chunk(gen, size))
        if len(chunk) == 0:
            break
        last_chunk = chunk

    print(last_chunk)

    return

def print_with_list(n, size=5):
    values = [i for i in range(n)]
    index = len(values) % size or size
    print(values[-index:])

MODE_MAP = {
    "list": print_with_list,
    "gen": print_with_gen,
}

def main(mode, n):
    try:
        n = int(n)
    except ValueError:
        print("n must be an integer")
        exit(1)
    try:
        MODE_MAP[mode](n)
    except KeyError:
        print("mode must be either list or gen")
        exit(1)
    return

if __name__ == "__main__":
    import sys
    try:
        _, mode, n = sys.argv
    except ValueError:
        print("use -> python -m chunk_gen [mode] [n]")
        exit(1)
    main(mode, n)

