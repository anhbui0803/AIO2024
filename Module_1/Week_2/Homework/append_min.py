def append_min(data, maxz, minz):
    res = []
    for i in data:
        # Your code here
        # Neu i < minz thi append minz vao res
        if i < minz:
            res.append(minz)
        elif i > maxz:
            res.append(maxz)
        else:
            res.append(i)

    return res


if __name__ == '__main__':
    assert append_min(data=[5, 2, 5, 0, 1], maxz=1, minz=0) == [1, 1, 1, 0, 1]
    print(append_min(data=[10, 2, 5, 0, 1], maxz=2, minz=1))  # [2, 2, 2, 1, 1]
