def test(_list, start, end):
    if start == end:
        for i in _list:
            print(i, end=" ")
        print("")
    for i in range(start, end):
        _list[i], _list[end] = _list[end], _list[i]
        test(_list, start + 1, end)
        _list[end], _list[i] = _list[i], _list[end]


if __name__ == '__main__':
    test_list = [1, 100, 10, 101]
    test(test_list, 0, len(test_list) - 1)
