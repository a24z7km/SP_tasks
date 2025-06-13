def front_back(a, b):
    # a の前半と後半を分割
    if len(a) % 2 == 0:
        a_front = a[:len(a)//2]
        a_back = a[len(a)//2:]
    else:
        a_front = a[:len(a)//2 + 1]
        a_back = a[len(a)//2 + 1:]

    # b の前半と後半を分割
    if len(b) % 2 == 0:
        b_front = b[:len(b)//2]
        b_back = b[len(b)//2:]
    else:
        b_front = b[:len(b)//2 + 1]
        b_back = b[len(b)//2 + 1:]

    # 前半と後半を組み合わせて返す
    return a_front + b_front + a_back + b_back

# テストケース
print(front_back('abcd', 'xy'))     # abxcdy
print(front_back('abcde', 'xyz'))   # abcxydez
print(front_back('Kitten', 'Donut')) # KitDontenut