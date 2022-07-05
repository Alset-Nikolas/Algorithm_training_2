
def check(text: str):
    balance = 0
    for t in text:
        if t == '(':
            balance += 1
        elif t == ')':
            if balance == 0:
                return False
            balance -= 1
    return balance == 0

if __name__ == '__main__':
    info = input()
    bool_ans = check(info)
    if bool_ans:
        print('YES')
    else:
        print('NO')
    assert check('(())()') == 1
    assert  check('(()))()') == 0
