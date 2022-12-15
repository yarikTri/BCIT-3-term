from random import randint


def gen_random_1(num_count, begin, end):
    return (randint(begin, end) for i in range(num_count))

def gen_random_2(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)

gen_random = gen_random_1

if __name__ == "__main__":
    for i in gen_random(6, 1, 3):
        print(i)
