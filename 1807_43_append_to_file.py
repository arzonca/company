def append_line_to_file(path, text_line):   #dopisywanie do pliku   <ctrl> lewy z wskazaniem nazwy funkcji myszką otwiera manual
    with open(path, 'a') as f:
        f.write("{}\n".format(text_line))


if __name__== '__main__':
    append_line_to_file("appending.txt", "Ewa")