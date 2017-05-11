def is_lake(map_given, coord, seen=None):
    """Determines whether coordinate is part of a lake or not."""

    if not seen:
        seen = set()
        seen.add(coord)

    print "seen is %s" % seen
    print "coord is", coord
    off_grid = [0, len(map_given) - 1, -1]

    if coord[0] in off_grid or coord[1] in off_grid:
        print "IM IN THE OFF GRID STATEMENT"
        return False

    # Loop through coordinates around coordinate
    coords_to_check = [(coord[0] + 1, coord[1]),
                       (coord[0] - 1, coord[1]),
                       (coord[0], coord[1] + 1),
                       (coord[0], coord[1] - 1)
                      ]

    for c in coords_to_check:
        print "c is ", c
        if c in seen:
            continue
        else:
            seen.add(c)
            if map_given[c[0]][c[1]] == 'l':
                continue
            else:
                print "In else to rerun function"
                if not is_lake(map_given, c, seen):
                    return False
    return True


map_test = ['llll',
            'lwwl',
            'lwww',
            'llwl'
            ]

coordinate = (1, 1)

chris_map = [
            'lllll',
            'lwwll',
            'llwll',
            'llwll',
            'lllll'
            ]

print is_lake(chris_map, coordinate)
