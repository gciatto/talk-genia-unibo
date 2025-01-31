# Creates an ordered copy of xs, via the Bubble Sort algorithm
def bubble_sort(xs: list):
    xs = xs.copy()
    n = len(xs)
    for i in range(n):
        for j in range(n - 1 - i):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs


items = [3, 1, 4, 1, 5, 9, 2, 6]
ordered = bubble_sort(items)
assert ordered == [1, 1, 2, 3, 4, 5, 6, 9], f"Wrong result: {ordered}"
print("ok")
