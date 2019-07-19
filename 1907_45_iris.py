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
        dictionary = {'Iris-setosa': [], 'Iris-versicolor': [], 'Iris-virginica': []}  #dict comprehension
        for element in self.data:   #iterujemy po wszytskich linijkach tablicy krotek
            if element[4] == 'Iris-setosa':
                dictionary['Iris-setosa'].append(element[:4])    #do listy bedącej wartością słownika disctionary pod kluczem 'Iris-setosa' /   dictionary['Iris-setosa'].   /
                # dołaczamy wszystkie elementy oprócz tego pod indekskem 4
            elif element[4] == 'Iris-versicolor':
                dictionary['Iris-versicolor'].append(element[:4])
            elif element[4] == 'Iris-virginica':
                dictionary['Iris-versicolor'].append(element[:4])
        return dictionary



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


