def cmp(coord1, coord2):
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]
    midx = (x1 + x2) / 2
    midy = (y1 + y2) / 2
    return((midx, midy))

print(cmp((0, 1), (5, 6)))