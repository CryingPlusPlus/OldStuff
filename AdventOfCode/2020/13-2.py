def to_bus_id(bus_IDs):
    bus_IDs = bus_IDs.split(',')
    bus_IDs = [(i, int(el)) for i, el in enumerate(bus_IDs) if el != 'x']

    return bus_IDs

def valid(time, bus_IDs):
    for offset, bus in bus_IDs:
        if (time + offset) % bus != 0:
            return False
    return True

def time(bus_IDs):
    time = 100000000000000

    while True:
        print(time)
        if valid(time, bus_IDs):
            return time
        time += 1

def main():
    bus_id = to_bus_id('29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,19,x,x,x,23,x,x,x,x,x,x,x,353,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41')
    print(time(bus_id))

if __name__ == "__main__":
    main()