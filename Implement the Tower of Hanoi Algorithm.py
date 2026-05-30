def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = ['{} {} {}'.format(rods[0], rods[1], rods[2])]

    def move(disks, source, auxiliary, target):
        if disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            states.append('{} {} {}'.format(rods[0], rods[1], rods[2]))
            return

        move(disks - 1, source, target, auxiliary)

        disk = rods[source].pop()
        rods[target].append(disk)
        states.append('{} {} {}'.format(rods[0], rods[1], rods[2]))

        move(disks - 1, auxiliary, source, target)

    move(n, 0, 1, 2)

    return '\n'.join(states)