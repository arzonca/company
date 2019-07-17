def print_lines_in_files(path):       #wypisuje z pliku na ekran
    with open(path) as f:   #otwiera plik i przypcisuje ten plik do zmiennej f
        print()
        for line in f:
            line = line.strip()   # funkcja strip na obieicie line usuwa biały znak konca linii (line to obiekt napis)
            print(line)


def read_lines_in_file(path):    #czyta plik do listy
    with open(path) as f:
        return [line.strip() for line in f]




if __name__ == '__main__':
    print_lines_in_files('tasks.txt')
    lines = read_lines_in_file('tasks.txt')
    print(lines)





