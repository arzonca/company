def write_line(path, text_line):   #funkcja nadpisuje za kazdym razem te sama linijke
    with open(path, 'w') as f:           #open domyslnie jest w mode = 'r'   open(path, 'r') czyli do czytania, trzeba dać 'w' - automatycznie sie tworzy plik
        f.write(text_line)


def write_line_twice(path, text_line):   #funkcja nadpisuje za kazdym razem te sama linijke
    with open(path, 'w') as f:           #open domyslnie jest w mode = 'r'   open(path, 'r') czyli do czytania, trzeba dać 'w' - automatycznie sie tworzy plik
        f.write("{}\n".format(text_line))    #\n - znak nowej linii
        f.write(text_line)


def write_to_file(path, names):      #zapisywaie linijka po linijce wg listy
    with open(path, 'w') as f:
        for name in names:
            f.write("{}\n".format(name))




if __name__== '__main__':
    write_line('writing.txt', "Ala ma kota2")
    write_line_twice('writing2.txt', "Ala ma kota2")
    write_to_file('writing3.txt', ["Maciek", "Kazek", "Tadek"])
