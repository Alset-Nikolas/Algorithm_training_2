def main(text):
    zerkalo = text[::-1]
    res = 0
    for i in range(len(text) // 2):
        if zerkalo[:len(text) // 2] != text[:len(text) // 2]:
            if zerkalo[i] != text[i]:
                zerkalo = zerkalo[:i] + text[i] + zerkalo[i + 1:]
                res += 1
        else:
            break
    return res


if __name__ == '__main__':
    text = input()
    res = main(text)
    print(res)

    assert main("a") == 0
    assert main("ab") == 1
    assert main("cognitive") == 4
