class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def first(self):
        return self.queue[0]

    def last(self):
        return self.queue[-1]


def search_portal(width, height, room):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    queue = Queue()
    visited = set()

    if len(room) != height or any(len(row) != width for row in room):
        print("Invalid map input.")
        return

    for y, floor in enumerate(room):
        for x, tile in enumerate(floor):
            if tile == 'F':
                queue.enqueue((x, y))
                visited.add((x, y))

    while not queue.is_empty():
        print(f'Queue: {queue.queue}')

        currentX, currentY = queue.dequeue()

        if room[currentY][currentX] == 'O':
            print('Found the exit portal.')
            return

        for dx, dy in directions:
            nextX, nextY = currentX + dx, currentY + dy
            if (0 <= nextX < width and 0 <= nextY < height and
                    room[nextY][nextX] in '_O' and (nextX, nextY) not in visited):
                queue.enqueue((nextX, nextY))
                visited.add((nextX, nextY))

    print('Cannot reach the exit portal.')


if __name__ == '__main__':
    width, height, room = 8, 6, [
        "########",
        "##___###",
        "##_F_###",
        "##____##",
        "##_##_O_",
        "##______"
    ]
    search_portal(width, height, room)
