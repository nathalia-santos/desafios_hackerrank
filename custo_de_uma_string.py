def h(n, k):
    fn, gn = k, 0
    for _ in range(n):
        hn = fn + gn
        fn, gn = (k - 1) * (fn + gn), fn
    return hn