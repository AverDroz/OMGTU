import math

def xd(put1):
    with open(put1, "r") as file:
        a, b, c = map(int, file.readline().split())
        sa, sb, sc = map(int, file.readline().split())
        fa, fb, fc = map(int, file.readline().split())

    if abs(sa - fa) == a:
        return min(((c - fc + c - sc + a) ** 2 + (abs(sb - fb) ** 2)) ** 0.5, 
                   ((fc + sc + a) ** 2 + (abs(sb - fb) ** 2)) ** 0.5, 
                   ((b - fb + b - sb + a) ** 2 + (abs(sc - fc) ** 2)) ** 0.5, 
                   ((fb + sb + a) ** 2 + (abs(sc - fc) ** 2)) ** 0.5)
    elif abs(sb - fb) == b:
        return min(((a - fa + a - sa + b) ** 2 + (abs(sc - fc) ** 2)) ** 0.5, 
                   ((fa + sa + b) ** 2 + (abs(sc - fc) ** 2)) ** 0.5, 
                   ((c - fc + c - sc + b) ** 2 + (abs(sa - fa) ** 2)) ** 0.5, 
                   ((fc + sc + b) ** 2 + (abs(sa - fa) ** 2)) ** 0.5)
    elif abs(sc - fc) == c:
        return min(((a - fa + a - sa + c) ** 2 + (abs(sb - fb) ** 2)) ** 0.5, 
                   ((fa + sa + c) ** 2 + (abs(sb - fb) ** 2)) ** 0.5, 
                   ((b - fb + b - sb + c) ** 2 + (abs(sa - fa) ** 2)) ** 0.5, 
                   ((fb + sb + c) ** 2 + (abs(sa - fa) ** 2)) ** 0.5)
    else:
        if ((sa == 0 or sa == a) and (fb == 0 or fb == b)) or ((fa == 0 or fa == a) and (sb == 0 or sb == b)):
            return ((abs(sc - fc) ** 2 + (abs(sa - fa) + abs(sb - fb)) ** 2) ** 0.5)
        elif ((sc == 0 or sc == c) and (fb == 0 or fb == b)) or ((fc == 0 or fc == c) and (sb == 0 or sb == b)):
            return ((abs(sa - fa) ** 2 + (abs(sc - fc) + abs(sb - fb)) ** 2) ** 0.5)
        else:
            return ((abs(sb - fb) ** 2 + (abs(sa - fa) + abs(sc - fc)) ** 2) ** 0.5)