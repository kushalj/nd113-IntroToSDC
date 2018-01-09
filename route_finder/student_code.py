
# Warning! this function will (unobtrusively) mutate M.intersections
# (see node_cost() function below for details)
def shortest_path(M, start, goal):
    print("shortest path called.", )

    # Assertions added as per suggestion
    assert( type(M.intersections) is dict )
    assert( type(M.roads) is list )
    assert( type(start) is int and type(goal) is int )

    result = shortest_path_tests()
    if not result[0]:
        raise RuntimeError(str('Error: '+result[1]+' failed.'))


    # Frontier Model initialization:
    # chose list() as we will need to access paths at a specific
    # index (for path selection)
    # frontier = list [path, path, ... ]

    # chose list() as we will need to maintain ordering
    # path = list [ intersection, intersection, ... ]

    frontier = [
        [start]
    ]


    # for explored intersections ids
    # chose set() as we need to have rapid lookups of existing data
    # and don't need ordering
    explored = set([])


    # paths
    # shortest_path_key = None
    shortest_complete_path = None
    f_shortest_complete_path = None

    # current_path_key = None
    current_path = None
    f_current_path = None


    # FRONTIER EXPLORATION LOOP
    # safety valve for testing:
    # loops = 0

    while len(frontier):
        # safety valve for testing:
        # if loops > 100:
        #    break

        # chosen path[] will no longer be in frontier
        current_path = remove_shortest_path(frontier, M.intersections, goal)

        # calculate f (A_star) of the path
        f_current_path = f_(M.intersections, current_path, goal)

        # if we have a shortest complete and current_path (uncomplete)
        # is already longer/same as shortest_complete_path, skip this path
        # (which will abandon the path)
        if f_shortest_complete_path and f_current_path >= f_shortest_complete_path:
            # we have already removed the path so we just skip the rest of the loop:
            continue

        # state = our location (end of the shortest path chosen above)
        state = current_path[-1]

        # does state = goal? Then we are done --> check f() of path; save
        if state == goal:

            # If none complete, save this as a complete path
            if shortest_complete_path == None:
                # we have our first complete path
                shortest_complete_path = current_path
                f_shortest_complete_path = f_current_path

            # else if there is a complete, check if this is shorter; save
            elif f_shortest_complete_path > f_current_path:
                shortest_path = current_path
                f_shortest_path = f_current_path

        # we are not at the goal.
        # actions at state:
        # assess the state (current_path[-1]) and get unexplored intersections
        else:
            # find new paths from state
            new_paths = find_new_paths(M.roads, current_path, explored)

            # state is now explored
            explored.add(state)

            # add new paths to frontier
            expand_frontier(frontier, new_paths)

    print("Summary")
    print(start, "to", goal, ", explored: ", explored, ", frontier: ", frontier)
    print("shortest_complete_path: ", shortest_complete_path, "\n")

    return shortest_complete_path


# straight line cost from start(x,y) to end(x,y)
def node_cost(intersections, start, end):
    from math import sqrt

    # cache
    key = str(start)+"_"+str(end)
    if key in intersections.keys():
        return(intersections[key])

    # work out direct distance between intersections
    x = 0
    y = 1
    x_dist = abs( (intersections[end][x] - intersections[start][x]) )
    y_dist = abs( (intersections[end][y] - intersections[start][y]) )

    # calc euclidean distance as hueristic
    cost = sqrt(x_dist**2 + y_dist**2)

    # cache the result
    intersections[key] = cost

    return cost


def path_cost(path, intersections):
    # Now caches path cost as we go along (as per suggestion)

    cost = 0

    # check cache
    # key is the path as a string
    key = str(path)
    if key in intersections.keys():
        cost = (intersections[key])
        return cost


    # we may have the penultimate path cost
    if len(path) > 1:
        penultimate_key = str(path[:-1])
        if penultimate_key in intersections.keys():
            cost = (intersections[penultimate_key])

            # Testing: uncomment to view cached paths
            # print(path, penultimate_key, cost)

    if cost > 0: # and (assumed) len(path) >= 2
        # we have a partial cost. We just need the path[-2] to path[-1]
        cost += node_cost(intersections, path[-2], path[-1])
        # cache the result
        intersections[key] = cost

    else:
        # calculate full path
        for i in range(len(path)):
            if i+1 < len(path):
                intersectionA = path[i]
                intersectionB = path[i+1]
                cost += node_cost(intersections, intersectionA, intersectionB)

        # cache the result
        intersections[key] = cost

    return cost


def f_(intersections, path_list, goal):
    # check path_list as this will be referenced as a list
    if not isinstance(path_list, list):
        raise TypeError('path_list must be a list')

    # f = g+h
    f = None

    # g = explored path cost
    g = path_cost(path_list, intersections)

    # h = straight line from last explored to goal
    h = node_cost(intersections, path_list[-1], goal)

    f = g+h
    return f


# add path_list to frontier dict and return key
# frontier is a list of lists, path is a list
def add_path(frontier, path):
    frontier.append(path)

    path_index = len(frontier)-1
    return path_index


# remove and return path using dict-key
# frontier is a list of lists, index is a list index
def remove_path(frontier, index):
    #make copy of the path
    removed_path = frontier[index][:]

    del frontier[index]

    return removed_path


# frontier is a list of lists, intersections is a dict, goal is an int
def remove_shortest_path(frontier, intersections, goal):
    shortest_path_index = None
    f_shortest_path = None

    paths = set([])
    for path_index in range(len(frontier)):
        path = frontier[path_index]

        # get f_() (g+h) for this path
        f_path = f_(intersections, path, goal)

        # if we don't have a shortest or f_path is shorter than
        # current shortest, save this path as shortest
        if shortest_path_index is None or f_path < f_shortest_path:
            shortest_path_index = path_index
            f_shortest_path = f_path



    # save shortest path and remove path from frontier
    shortest_path = remove_path(frontier, shortest_path_index)

    # return removed path
    return shortest_path


# roads is a list of lists, current_path is a list, explored is a set
def find_new_paths(roads, current_path, explored):
    new_paths = []
    state = current_path[-1]   # intermediate variable makes code more readable

    # for every intersection in this road[state] list
    for intersection in roads[state]:
        # copy current path
        new_path = current_path[:]
        path_changed = False

        if intersection not in explored:
            path_changed = True
            new_path.append(intersection)
            new_paths.append(new_path)

    return new_paths


# frontier is a list of lists, new_paths is a list of lists
def expand_frontier(frontier, new_paths):
    for path in new_paths:
        add_path(frontier, path)



#################################################
# Quick tests to check the main happy paths only.
# these were used as a utility rather than as
# a full test suite.
def shortest_path_tests():

    result = (True, "Ok")

    test_intersections_1 = {
        0: [1, 1],
        1: [2, 2],
        2: [4, 4],
        3: [5, 5],
        4: [8, 8]
    }


    test_intersections_2 = {
        0: [0.7798606835438107, 0.6922727646627362],
        1: [0.7647837074641568, 0.3252670836724646],
        2: [0.7155217893995438, 0.20026498027300055],
        3: [0.7076566826610747, 0.3278339270610988],
        4: [0.8325506249953353, 0.02310946309985762],
        5: [0.49016747075266875, 0.5464878695400415],
        6: [0.8820353070895344, 0.6791919587749445],
        7: [0.46247219371675075, 0.6258061621642713],
        8: [0.11622158839385677, 0.11236327488812581],
        9: [0.1285377678230034, 0.3285840695698353]
    }


    test_frontier_1 = [
        [0, 1],
        [0, 1, 2],
        [2]
    ]


    test_frontier_2 = [
        [0]
    ]


    test_roads_1 = [
        [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
        [36, 34, 31, 28, 17],
        [39, 36, 21, 19, 28]
    ]

    test_roads_2 = [
        [7, 6, 5],
        [4, 3, 2],
        [4, 3, 1],
        [5, 4, 1, 2],
        [1, 2, 3],
        [7, 0, 3],
        [0],
        [0, 5],
        [9],
        [8]
    ]


    test_explored_1 = set([28, 17])


    test_explored_2 = set([])


    # new paths for path 0 in frontier [0, 1] uses
    # [36, 34, 31, 28, 17]
    # it should skip 28 and 17
    new_paths_0_result = [
        [0, 1, 36],
        [0, 1, 34],
        [0, 1, 31]
    ]

    # new paths for path 1 in frontier [0, 1, 2] uses
    # [39, 36, 21, 19, 28]
    # it should skip 28
    new_paths_1_result = [
        [0, 1, 2, 39],
        [0, 1, 2, 36],
        [0, 1, 2, 21],
        [0, 1, 2, 19]
    ]


    # node_cost test
    # node_cost: 2-1 + 2-1 = 2
    ti_result = 2

    if node_cost(test_intersections_1, 0, 1) is not ti_result:
        result = (False, "node_cost")


    # path_cost test
    # path_cost: 0-1: 2, 1-2: 4, 2+4 = 6
    pc_result = 6

    if path_cost(test_frontier_1[1], test_intersections_1) is not pc_result:
        result = (False, "path_cost")


    # f = g+h test
    # g = path_cost = pc_result
    # h = path[-1] to goal (2 to 3) = node_cost(2 to 3)
    gh_result = pc_result + node_cost(test_intersections_1, 2, 3)

    if f_(test_intersections_1, test_frontier_1[1], 3) is not gh_result:
        result = (False, "f=g+h test")


    # add_path test
    test_path_list = [1, 2]
    test_path_index = add_path(test_frontier_1, test_path_list)

    # check we get an int back (which is path id in frontier)
    if type(test_path_index) is not int:
        result = (False, "add_path")
    # print(test_frontier)

    # remove_path test
    frontier_length = len(test_frontier_1)
    result = remove_path(test_frontier_1, test_path_index)
    if type(result) is not list and len(test_frontier_1) is not frontier_length-1:
        result = (False, "remove_path")
    # print(test_frontier)


    # remove_shortest_path test
    # print(f_(test_intersections, test_frontier[0], 3))
    # print(f_(test_intersections, test_frontier[1], 3))
    # print(f_(test_intersections, test_frontier[2], 3))

    path = remove_shortest_path(test_frontier_1, test_intersections_1, 3)
    if path != [2]:
        result = (False, "remove_shortest_path")
    #print(path)


    # find_new_paths test
    # test with frontier[0]
    test_explored_A = test_explored_1.copy() # fresh explored set
    new_paths = find_new_paths(test_roads_1, test_frontier_1[0], test_explored_A)

    if tuple(new_paths) != tuple(new_paths_0_result):
        result = (False, "find_new_paths (test_frontier_1[0])")

    # test with frontier[1]
    test_explored_B = test_explored_1.copy() # fresh explored set
    new_paths = find_new_paths(test_roads_1, test_frontier_1[1], test_explored_B)

    if tuple(new_paths) != tuple(new_paths_1_result):
        result = (False, "find_new_paths (test_frontier_1[1])")
        print(new_paths, new_paths_1_result)


    # expand_frontier test
    frontier_length = len(test_frontier_1)
    num_paths = len(new_paths)
    expand_frontier(test_frontier_1, new_paths)

    if len(test_frontier_1) is not frontier_length+num_paths:
        result = (False, "expand_frontier")



    #print("---- END OF TESTS ----")

    return result




                            
