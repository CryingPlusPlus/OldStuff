import matplotlib.pyplot as plt
import numpy as np

class Person:
    def __init__(self, name, span):
        self.name = name
        self.span = span

def reader():
    with open('zeiten.txt', 'r') as fh:
        return ''.join(fh).split('\n')

wann_nicht_zeit = lambda span : [i for i in range(17, 93) if i not in span]
format_to_int = lambda some : int(some[0]) + {'06' : 0, '07' : 30, '08' : 61}[some[1]]

def create_span(data):
    end = []
    for span in data:
        start, schluss = span.split(' - ')
        start = format_to_int(start.split('.'))
        schluss = format_to_int(schluss.split('.'))
        for i in range(start, schluss + 1):
            end.append(i)
    return end

def create_person(data):
    data = data.split('    ')
    span = create_span(data[1:])
    span = wann_nicht_zeit(span)
    return Person(data[0].replace(':', ''), span)

def make_points(personen, wer_nicht = []):
    x = [i for i in range(17, 93)]
    y = [0 for _ in range(len(x))]

    for person in personen:
        if person.name not in wer_nicht:
            for day in person.span:
                y[day - 17] += 1
    return x, y

def plotter(x, y):
    plt.plot(x, y)
    plt.show()

def get_intervall(personen, start, schluss):
    intervall = [i for i in range(start, schluss + 1)]
    end = []
    for person in personen:
        for day in person.span:
            if day in intervall:
                end.append(person.name)
                break
    return end

def main():
    fh = reader()
    fh = ''.join(fh).split(';')
    personen = [create_person(pers_data) for pers_data in fh]
    personen.sort(key=(lambda e : len(e.span)))
    # for person in personen:
        # print(person.name, len(person.span))
    juni = get_intervall(personen, 17, 30)
    juli = get_intervall(personen, 31, 61)
    august = get_intervall(personen, 61, 93)
    print('Juni:', ', '.join(juni))
    print('Juli:', ', '.join(juli))
    print('August:', ', '.join(august))
    x, y = make_points(personen)
    plotter(x, y)


if __name__ == '__main__':
    main()
