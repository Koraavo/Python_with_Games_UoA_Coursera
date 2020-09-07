'''
def main():
    rec1_x = 5
    rec1_y = 10
    rec1_width = 15
    rec1_height = 20

    rec2_x = 10
    rec2_y = 5
    rec2_width = 20
    rec2_height = 15

    if rectangles_intersect(rec1_x, rec1_y, rec1_width, rec1_height, rec2_x, rec2_y, rec2_width, rec2_height):
        print('overlap')
    else:
        print('no overlap')


def rectangles_intersect(x1, y1, width, height, x2, y2, width2, height2):
    #return not ((x1 + width < x2) or (x2 + width2 < x1) or (y1 + height < y2) or (y2 + height2 < y1))
    return not (20 < 10 or 30 < 5 or 30 < 5 or 20 < 10)


main()
'''

def main():
    rect1 = create_rectangle(5, 10, 15, 20)
    rect2 = create_rectangle(10, 5, 20, 15)
    if rectangles_intersect(rect1, rect2):
        print('overlap')
    else:
        print('no overlap')

def create_rectangle(corner_x, corner_y, width, height):
    rect = Rectangle()
    rect.x = corner_x
    rect.y = corner_y
    rect.width = width
    rect.height = height
    return rect


def rectangles_intersect(r1, r2):
    #return not ((x1 + width < x2) or (x2 + width2 < x1) or (y1 + height < y2) or (y2 + height2 < y1))
    #return not (20 < 10 or 30 < 5 or 30 < 5 or 20 < 10)
    # return not ((r1.x + r1.width < r2.x) or (r2.x + r2.width < r1.x) or (r1.y + r1.height < r2.y) or (r2.y + r2.height < r1.y))
    return (r1.x + r1.width >= r2.x) or (r2.x + r2.width >= r1.x) or (r2.y + r2.height >= r1.y) or (
            r1.y + r1.height >= r2.y)


class Rectangle:
    pass

main()



