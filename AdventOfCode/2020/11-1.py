def reader():
    end = []
    with open('data.txt', 'r') as fh:
        for line in fh:
            line = line.split('\n')[0]
            end.append(line)
    return end


def count_around(seats, pos, char):
    compass = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
    end = 0
    for comp in compass:
        x = pos[1] + comp[1]
        y = pos[0] + comp[0]
        if 0 <= x < len(seats[0]) and 0 <= y < len(seats):
            if seats[y][x] == char:
                end += 1
    return end

def update_seats(seats):
    new_seats = []
    for y, row in enumerate(seats):
        new_row = ""
        for x, seat in enumerate(row):
            if seat == 'L':
                if count_around(seats, (y, x), '#') == 0:
                    new_row += '#'
                    continue
            if seat == '#':
                if count_around(seats, (y, x), '#') >= 4:
                    new_row += 'L'
                    continue
            new_row += seat
        new_seats.append(new_row)
    return new_seats

def looper(seats):
    new_seats = update_seats(seats)

    if new_seats == seats:
        return new_seats
    else:
        return looper(new_seats)

ersetzen = lambda seats : [1 if seat == '#' else 0 for row in seats for seat in row]

def main():
    seats = reader()
    seats = looper(seats)
    
    print(sum(ersetzen(seats)))
    
if __name__ == "__main__":
    main()