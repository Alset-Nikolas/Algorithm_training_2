def calc_distant(homes, shops):
    dist = 0
    if len(shops) == 2:
        lef_shop, right_shop = shops
        for h in homes:
            dist_h = min(abs(h - lef_shop), abs(right_shop - h))
            dist = max(dist, dist_h)
    if len(shops) == 1:
        shop = shops[0]
        for h in homes:
            dist_h = abs(h - shop)
            dist = max(dist, dist_h)
    return dist


def main(numbers):
    homes = []
    shops = []
    max_dist = 0
    for i, x in enumerate(numbers):
        if x == 0:
            continue
        if x == 1:
            homes.append(i)
        if x == 2:
            shops.append(i)
            if len(shops) > 2:
                shops = shops[1:]
            if homes:
                max_dist = max(calc_distant(homes, shops), max_dist)
                homes = []

    else:
        if homes:
            max_dist = max(calc_distant(homes, shops), max_dist)
    return max_dist


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    res = main(numbers)
    print(res)

    assert main([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3
