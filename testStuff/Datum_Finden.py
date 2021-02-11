def reader():
    with open('zeiten.txt', 'r') as fh:
        return ''.join([line.replace('\n', '') for line in fh])

class Person:
    def __init__(self, name, span):
        self.name = name
        self.span = span

def string_zeit_to_int(rang):
    to_zahl = {
        '06' : 0,
        '07' : 30,
        '08' : 61
    }
    start, schluss = rang.split(' - ')
    start = start.split('.')
    schluss = schluss.split('.')
    t_int = lambda some : int(some[0]) + to_zahl[some[1]]
    start = t_int(start)
    schluss = t_int(schluss)

    return start, schluss

def create_person(zeiten):
    end = []
    zeiten = zeiten.split('    ')
    for rang in zeiten[1:]:
        start, schluss = string_zeit_to_int(rang)
        for i in range(start, schluss + 1):
            end.append(i)
    return Person(zeiten[0], end)

def tester(time_span, personen):
    for person in personen:
        rem = []
        for i in time_span:
            if i not in person.span:
                rem.append(i)
        for i in rem:
            time_span.remove(i)
    return time_span

def main():
    zeiten = reader()
    zeiten = zeiten.split(';')
    time_span = [i for i in range(0, 61 + 31)]
    personen = [create_person(set) for set in zeiten]
    personen.sort(key=(lambda e : len(e.span)))
    for per in personen:
        print(per.name, len(per.span))
    print('Rem test: ')
    for i in range(len(personen)):
        temp = personen
        temp_time = time_span
        temp.pop(0)
        print('ohne ' + personen[0].name, len(tester(temp_time, temp)))


main()
