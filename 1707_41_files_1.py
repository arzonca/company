from company2 import Task     #importujemy klasę Task z


def read_tasks_from_file(path):    #czyta plik do listy obiektów
    tasks = []
    with open(path) as f:  # otwiera plik i przypcisuje ten plik do zmiennej f
        for line in f:
            line = line.strip()
            line = line.split(";")# funkcja strip na obieicie line usuwa biały znak konca linii (line to obiekt napis)
            description = line[0]
            points = int(line[1])
            tasks.append(Task(description, points))
    return tasks




if __name__ == '__main__':
    # print_lines_in_files('tasks1.txt')
    # lines = read_lines_in_file('tasks1.txt')
    # print(lines)
    print(read_tasks_from_file('tasks1.txt'))





