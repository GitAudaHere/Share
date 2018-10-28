try:
    file = open("/home/chen/Desktop/USACO Practice/2016DecGold3/input.txt", "r")
    lines = list(map(lambda line: line.strip(), file.readlines()))
    first_line = lines[0].split()
    num_fences = int(first_line[0])
    laser_coord = [int(first_line[1]), int(first_line[2])]
    barn_coord = [int(first_line[3]), int(first_line[4])]
    fence_coords = list(map(lambda line: [int(line.split()[0]), int(line.split()[1])], lines[1:]))
    print(fence_coords, num_fences, laser_coord, barn_coord, sep="\n")

    fence_coords_x = list(map(lambda coord: coord[0], fence_coords))
    fence_coords_y = list(map(lambda coord: coord[1], fence_coords))
    
    # Creates two lists of indices of the x coordinates and y coordinates of the fences that only show up once
    out_of_range_index_x = [i for i, x in enumerate(fence_coords_x) if fence_coords_x.count(x) == 1]
    out_of_range_index_y = [i for i, y in enumerate(fence_coords_y) if fence_coords_y.count(y) == 1]

    # A set of the indices of the two lists that contain the same indices
    unusable_fences = set(out_of_range_index_x).intersection(out_of_range_index_y)

    usable_fences = []
    for i in range(len(fence_coords)):
        if i not in unusable_fences:
            usable_fences.append(fence_coords[i])
    print(usable_fences)

    def find_path(ref_coord, start_coord, usable_paths, used_paths=[], steps=0):
        if start_coord[0] == laser_coord[0] or start_coord[1] == laser_coord[1]:
            print(start_coord, laser_coord)
            return steps + 1
        elif len(usable_paths) == 0:
            return -1
        else:
            print(steps)
            used_paths.append(start_coord)
            usable_paths = list(set(tuple(i) for i in usable_paths) - set(tuple(i) for i in used_paths))
            print(usable_paths)
            if start_coord[1] == ref_coord[1]:
                for path in usable_paths:
                    if path[0] == start_coord[0]:
                        find_path(start_coord, path, usable_paths, used_paths, steps + 1)
            else:
                for path in usable_paths:
                    if path[1] == start_coord[1]:
                        find_path(start_coord, path, usable_paths, used_paths, steps + 1)

    print(find_path(barn_coord, usable_fences[2], usable_fences))

finally:
    file.close()
