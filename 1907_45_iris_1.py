class IrisLoader:
    def __init__(self):
        self.data = []

    def load(self, path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                line = line.split(",")
                v0 = float(line[0])
                v1 = float(line[1])
                v2 = float(line[2])
                v3 = float(line[3])
                name = line[4]

                self.data.append((v0, v1, v2, v3, name))

    def iris_dict(self):

        dictionary = {}   #pusty słownik
        for element in self.data:
            key = element[4]   # jako key podstawiamy ostatnie pole elementu

            if key not in dictionary:   # jesli klucz nie istbnieje to go otwórz
                dictionary[key] = []
            dictionary[key].append(element[:4]) #tak czy siak dodaj wszytskie pola oprócz czwartego do istniejącego juz
            # klucza w  w słowniku

        return dictionary

def pretty_print_dictionary(dictionary):
    for key, value in dictionary.items():
        print("{}: {}".format(key, value))




                # for i in line:
                #     if i < 4:
                #         line[i] = float(line[i])
                #     else:
                #         line[5] = line[i]
                # self.data.append(line)

if __name__ == '__main__':
    loader = IrisLoader()
    loader.load('iris.data')
    print(loader.data[:2])
    my_dictionary = loader.iris_dict()
    print(my_dictionary)
    print()
    pretty_print_dictionary(my_dictionary)


