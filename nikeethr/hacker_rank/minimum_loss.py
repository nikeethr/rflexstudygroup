def merge_sort(x):
    l = len(x)

    if l > 1:
        m = l // 2
        left = x[:m]
        right = x[m:]

        merge_sort(left)
        merge_sort(right)

        ll = len(left)
        lr = len(right)

        i = 0
        j = 0
        k = 0

        while i < ll and j < lr:
            if left[i] < right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1

        while i < ll:
            x[k] = left[i]
            i += 1
            k += 1

        while j < lr:
            x[k] = right[j]
            j += 1
            k += 1

def binary_search(x, i):
    s = 0
    e = len(x)
    m = len(x) // 2

    while True:
        if i > x[m]:
            s = m
        elif i < x[m]:
            e = m
        else:
            return m

        m_ = m
        m = (e + s) // 2

        if m_ == m:
            return m

def min_loss(p):
    p_s = p.copy()
    merge_sort(p_s)
    loss = 1e16

    for i in p:
        j = binary_search(p_s, i)
        if (j+1) < len(p_s) and p_s[j] >= p_s[j+1] and loss > p_s[j] - p_s[j+1]:
            loss = p_s[j] - p_s[j+1]
        if (j-1) >= 0 and p_s[j] >= p_s[j-1] and loss > p_s[j] - p_s[j-1]:
            loss = p_s[j] - p_s[j-1]
        if loss == 0:
            return 0
        p_s.pop(j)

    return loss

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    loss = min_loss(p)
    print(loss)
