def main(sum_points, last_points):
    all_numbers = set()
    numbers_repeat = set()
    losers_best = 0
    answer = 1

    for number in last_points:
        if number in all_numbers:
            numbers_repeat.add(number)
        all_numbers.add(number)
    all_numbers.remove(0)
    for peter_number in range(1, 102):
        all_numbers_i = all_numbers.copy()
        numbers_repeat_i = numbers_repeat.copy()
        people_point = sum_points.copy()
        last_points_i = last_points.copy()
        last_points_i[-1] = peter_number

        if peter_number in all_numbers:
            numbers_repeat_i.add(peter_number)
        all_numbers_i.add(peter_number)
        winner = None
        for number in sorted(list(all_numbers_i)):
            if number not in numbers_repeat_i:
                winner = number
                break
        for i in range(len(people_point)):
            if last_points_i[i] == winner:
                people_point[i] += last_points_i[i]
                break
        peter_point = people_point[-1]
        losers_now = 0

        for point in people_point:
            if point < peter_point:
                losers_now += 1

        if losers_now > losers_best:
            losers_best = losers_now
            answer = peter_number
    return answer


if __name__ == '__main__':
    n = int(input())
    sum_points = list(map(int, input().split()))
    last_points = list(map(int, input().split()))
    last_points.append(0)
    res = main(sum_points, last_points)
    print(res)
