import copy
grund = [[1], [1], [2], [2], [3], [3]]
deepness = 2


def ergeb(current_grund, grund, current_deepness, deepness):
    mod = current_grund.copy()
    if current_deepness == 0:
        current_ground = grund.copy()
        ergeb(current_ground, grund, current_deepness + 1, deepness)
    elif current_deepness < deepness:
        end = []
        for elem in mod:
            for elem_g in grund:
                end.append(elem + elem_g)

        return ergeb(end, grund, current_deepness + 1, deepness)
    else:
        print(current_grund)


ergeb([], grund, 0, deepness)
