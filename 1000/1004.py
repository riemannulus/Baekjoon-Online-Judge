import sys
from math import sqrt

case = int(sys.stdin.readline())

while case > 0:
    start_end = list(map(int, sys.stdin.readline().split()))
    start = (start_end[0], start_end[1])
    end = (start_end[2], start_end[3])

    case2 = int(sys.stdin.readline())
    result = 0
    while case2 > 0:
        circle = list(map(int, sys.stdin.readline().split()))
        status = 0

        # 거리 구하는 식
        fn = lambda x2, y2, x1, y1: sqrt((x2-x1)**2 + (y2-y1)**2)

        """
        1. 원이 주어지면 원의 중점과 시작점까지의 거리가 원의 반지름 내에
        존재하는가를 검사: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        """
        if fn(circle[0], circle[1], start[0], start[1]) < circle[2]:
            result = result + 1
            status = status + 1

        """
        2. 원이 주어지면 원의 중점과 종점까지의 거리가 원의 반지름 내에
        존재하는가를 검사: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        """
        if fn(circle[0], circle[1], end[0], end[1]) < circle[2]:
            result = result + 1
            status = status + 1

        """
        3. 만약 둘 다 안에 존재한다면 시작점과 끝 점을 둘 다 가지고 있는
        큰 원이 있음을 뜻함. 이럴 경우는 제외해야 하므로 status가 2 이상인
        경우에는 1번과 2번에서 중복된 횟수를 뺀다.
        """
        if status > 1:
            result = result - 2

        case2 = case2 - 1

    print(result)
    case = case - 1
