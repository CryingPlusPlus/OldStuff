def main():
    bus_IDs = to_bus_id('29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,19,x,x,x,23,x,x,x,x,x,x,x,353,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41')
    print(looper(bus_IDs))

valid = lambda offset, bus, time : (time + offset) % bus == 0

def valid_for_all(bus_IDs, time):
    for offset, bus in bus_IDs:
        if not valid(offset, bus, time):
            return False
    return True

def get_max(bus_IDs):
    temp = [bus for _, bus in bus_IDs]
    temp = max(temp)
    for offset, bus in bus_IDs:
        if bus == temp:
            return offset, bus

def looper(bus_IDs):
    offset, mult = get_max(bus_IDs)
    index = (100000000000000 + offset) // mult

    while True:
        time = index * mult - offset
        print(time)
        if valid_for_all(bus_IDs, time):
            return time
        index += 1

def to_bus_id(bus_IDs):
    bus_IDs = bus_IDs.split(',')
    bus_IDs = [(i, int(el)) for i, el in enumerate(bus_IDs) if el != 'x']

    return bus_IDs

if __name__ == "__main__":
    main()