if __name__ == '__main__':
    n = int(input())
    new_event = input()
    all_numbers = set(range(1, n+1))
    while new_event != "HELP":

        new_event = set(map(int,new_event.split()))
        flag = True if input()=="YES" else False
        if flag:
            all_numbers &=  new_event
        else:
            all_numbers -= new_event
        new_event = input()
    print(*sorted(list(all_numbers)))