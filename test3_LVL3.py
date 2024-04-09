'''
You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
Output:
    11
'''
def solution(map):
    w, h = len(map), len(map[0])

    def tryAgain():
        visited = [[False] * h for i in range(w)]
        visited[0][0] = True

        q, i = [(0, 0, 1)], 0
        while i < len(q):
            x, y, length = q[i]
            i += 1
            if x == w - 1 and y == h - 1:
                return length
            
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < w and ny >= 0 and ny < h: # valid coord
                    if map[nx][ny] == 1:
                        continue
                    if visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny, length + 1))

        return None # Not solvable

    ans = tryAgain()
    
    for i in range(w):
        for j in range(h):
            if (i, j) in [(0, 0), (w-1, h-1)] or map[i][j] == 0:
                continue
            map[i][j] = 0
            newAns = tryAgain()
            if ans is None or (newAns is not None and ans > newAns):
                ans = newAns
            map[i][j] = 1

    return ans

if __name__ == "__main__":
    import sys

    print(solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 15)

    print(solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 13)

    print(solution([
        [0, 1],
        [1, 0],
    ]) == 3)

    print(solution([
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
     ]) == 7)

    print(solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 11)