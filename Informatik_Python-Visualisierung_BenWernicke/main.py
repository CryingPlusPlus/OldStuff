from matplotlib import pyplot as plt
import plotly.express as px
import numpy as np

def reader():
    with open('Musik.csv', 'r', encoding='utf8') as fh:
        return [line.replace('\n', '').split(';') for line in fh]

#Nur ein bisschen formatieren auf Sekunden und wegschmeißen von Liedtiteln und den anderen Informationen
format_to_time = lambda songs : [int(song[-1].split(':')[0]) * 60 + int(song[-1].split(':')[1]) for song in songs if ':' in song[-1]]

#Die einzelnen  Abschnitte berechnen
calc_bins = lambda songs, offset : [i for i in range(0, max(songs) + offset, offset)]

def input_Handler():
    songs = reader()
    songs = format_to_time(songs)
    bins = calc_bins(songs, 15)
    return songs, bins

def plotter(songs, bins):
    #hier die Lösung mit Matplotlib mit plotly hab ich es nur so komisch zum laufen bekommen - also es hat sich kein Fenster geöffnet sondern es wurde eine Datei erzeugt die mir dann im Browser angezeigt werden konnte (?)
    a = np.array(songs)
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(a, bins = bins)
    plt.show()

def main():
    songs, bins = input_Handler()
    print('Länge:', len(songs), 'Songs\tSpielzeit:', sum(songs), 'Sekunden')
    #lösung mit matplotlib
    plotter(songs, bins)

if __name__ == '__main__':
    main()
