import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss


def extender():                #Erstellung des Boxplots(hauptsächlich)
    plt.figure()
    plt.plot(time_lists)

    Summep0 = 0
    Summep1 = 0
    Summep2 = 0
    Summe = 0
    Summe2 = 0
    plt.legend()
    plt.title(cat)
    plt.figure()
    counter = 0
    data = []
    print(time_lists)
    print('now js')
    for j in time_lists:
        data.append(j)
        counter += 1
    plt.boxplot(data, positions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], labels=['base line', '6Hz +3BPM', '6Hz -3BPM',
                                                                         '6Hz -6BPM', '8Hz +3BPM', '8Hz -3BPM',
                                                                         '8Hz -6BPM', '10Hz +3BPM', '10Hz -3BPM',
                                                                         '10Hz -6BPM'])
    plt.title(cat)




#print('chose a file by number')
#files = ['res_1f.nl', 'results.nl', 'results.tf', 'results(1).nl', 'results(1).tf']
files = ['res_1f.nl', 'results.nl', 'results.tf',]
for file in files:
    print(file)
    print(file)
    print(file)
    print(file)
    if file == 'res_1f.nl' or file == 'results.nl' or file == 'results.tf':
        v = 10
    else:
        v = 60    #veraltet 
#print(files)
#inp = int(input())
#file = files[inp]
    X = pd.read_csv(file, sep="\t")                                                                        #Sortierung der HRV-Parameter
    df = X.replace('10', 'z0', regex=True)
    df = df.replace('11', 'z1', regex=True)
    df = df.replace(('pa1ph1', 'pa1ph2', 'pa1ph3', 'pa1ph5', 'pa1ph6', 'pa1ph7', 'pa1ph9', 'pa1phz0', 'pa1phz1'),
                    ('pa1ph9', 'pa1phz0', 'pa1phz1', 'pa1ph1', 'pa1ph2', 'pa1ph3', 'pa1ph5', 'pa1ph6', 'pa1ph7'), regex=True)
    df = df.replace(('pa3ph1', 'pa3ph2', 'pa3ph3', 'pa3ph5', 'pa3ph6', 'pa3ph7'),
                    ('pa3ph5', 'pa3ph6', 'pa3ph7', 'pa3ph1', 'pa3ph2', 'pa3ph3'), regex=True)
    df = df.replace(('pa4ph1', 'pa4ph2', 'pa4ph3', 'pa4ph9', 'pa4phz0', 'pa4phz1'),
                    ('pa4ph9', 'pa4phz0', 'pa4phz1', 'pa4ph1', 'pa4ph2', 'pa4ph3'), regex=True)
    df = df.replace(('pa6ph1', 'pa6ph2', 'pa6ph3', 'pa6ph5', 'pa6ph6', 'pa6ph7', 'pa6ph9', 'pa6phz0', 'pa6phz1'),
                    ('pa6ph5', 'pa6ph6', 'pa6ph7', 'pa6ph9', 'pa6phz0', 'pa6phz1', 'pa6ph1', 'pa6ph2', 'pa6ph3'),
                    regex=True)
    df = df.replace(('pa7ph1', 'pa7ph2', 'pa7ph3', 'pa7ph5', 'pa7ph6', 'pa7ph7'),
                    ('pa7ph5', 'pa7ph6', 'pa7ph7', 'pa7ph1', 'pa7ph2', 'pa7ph3'), regex=True)
    df = df.replace(('pa8ph1', 'pa8ph2', 'pa8ph3', 'pa8ph5', 'pa8ph6', 'pa8ph7'),
                    ('pa8ph5', 'pa8ph6', 'pa8ph7', 'pa8ph1', 'pa8ph2', 'pa8ph3'), regex=True)
    df = df.replace(('pa9ph1', 'pa9ph2', 'pa9ph3', 'pa9ph5', 'pa9ph6', 'pa9ph7', 'pa9ph9', 'pa9phz0', 'pa9phz1'),
                    ('pa9ph9', 'pa9phz0', 'pa9phz1', 'pa9ph1', 'pa9ph2', 'pa9ph3', 'pa9ph5', 'pa9ph6', 'pa9ph7'),
                    regex=True)
    df = df.replace(('pa10ph5', 'pa10ph6', 'pa10ph7', 'pa10ph9', 'pa10phz0', 'pa10phz1'),
                    ('pa10ph9', 'pa10phz0', 'pa10phz1', 'pa10ph5', 'pa10ph6', 'pa10ph7'), regex=True)
    df = df.replace(('PA1PH1', 'PA1PH2', 'PA1PH3', 'PA1PH5', 'PA1PH6', 'PA1PH7', 'PA1PH9', 'PA1PHZ0', 'PA1PHZ1'),
                    ('PA1PH9', 'PA1PHZ0', 'PA1PHZ1', 'PA1PH1', 'PA1PH2', 'PA1PH3', 'PA1PH5', 'PA1PH6', 'PA1PH7'),
                    regex=True)
    df = df.replace(('PA3PH1', 'PA3PH2', 'PA3PH3', 'PA3PH5', 'PA3PH6', 'PA3PH7'),
                    ('PA3PH5', 'PA3PH6', 'PA3PH7', 'PA3PH1', 'PA3PH2', 'PA3PH3'), regex=True)
    df = df.replace(('PA4PH1', 'PA4PH2', 'PA4PH3', 'PA4PH9', 'PA4PHZ0', 'PA4PHZ1'),
                    ('PA4PH9', 'PA4PHZ0', 'PA4PHZ1', 'PA4PH1', 'PA4PH2', 'PA4PH3'), regex=True)
    df = df.replace(('PA6PH1', 'PA6PH2', 'PA6PH3', 'PA6PH5', 'PA6PH6', 'PA6PH7', 'PA6PH9', 'PA6PHZ0', 'PA6PHZ1'),
                    ('PA6PH5', 'PA6PH6', 'PA6PH7', 'PA6PH9', 'PA6PHZ0', 'PA6PHZ1', 'PA6PH1', 'PA6PH2', 'PA6PH3'),
                    regex=True)
    df = df.replace(('PA7PH1', 'PA7PH2', 'PA7PH3', 'PA7PH5', 'PA7PH6', 'PA7PH7'),
                    ('PA7PH5', 'PA7PH6', 'PA7PH7', 'PA7PH1', 'PA7PH2', 'PA7PH3'), regex=True)
    df = df.replace(('PA8PH1', 'PA8PH2', 'PA8PH3', 'PA8PH5', 'PA8PH6', 'PA8PH7'),
                    ('PA8PH5', 'PA8PH6', 'PA8PH7', 'PA8PH1', 'PA8PH2', 'PA8PH3'), regex=True)
    df = df.replace(('PA9PH1', 'PA9PH2', 'PA9PH3', 'PA9PH5', 'PA9PH6', 'PA9PH7', 'PA9PH9', 'PA9PHZ0', 'PA9PHZ1'),
                    ('PA9PH9', 'PA9PHZ0', 'PA9PHZ1', 'PA9PH1', 'PA9PH2', 'PA9PH3', 'PA9PH5', 'PA9PH6', 'PA9PH7'),
                    regex=True)
    df = df.replace(('P10PH5', 'P10PH6', 'P10PH7', 'P10PH9', 'P10PHZ0', 'P10PHZ1'),
                    ('P10PH9', 'P10PHZ0', 'P10PHZ1', 'P10PH5', 'P10PH6', 'P10PH7'), regex=True)

    df = df.sort_values(by=['filename'])
    df = df.reset_index(drop=True)
    headers = list(X.columns.values)
    #print('chose a category by number')
    count = 0
    for i in headers:
        if i == "filename":                                          # Übersprinngen von nutzlosen Daten
            continue
        if i in ("Unnamed: 3", "totime", 'fromtime', 'Unnamed: 40'):
            continue
    #inp = int(input())
    #cat = headers[inp]
        cat = i
        print(cat)
        i = 0
        d = {}
        while i < 10:                                        #auslesen der Daten in Schrittenvon 10 da es 10 Phasen pro Testperson gab
            x = i * v

            result = df.loc[(df.index < x + v) & (df.index >= x + 0)]
            if cat == 'PHVAR100':                                        #veraltete Fehlersuche
                print(result[cat])
            d["Pa{0}".format(i + 1)] = result[cat].tolist()
            i = i + 1

        if v == 60:
            time_lists = [[] for _ in range(v-6)]  # Erstelle v leere Listen
        else:
            time_lists = [[] for _ in range(v)]  # Erstelle v leere Listen
            percent_lists = [[] for _ in range(v - 1)]
        for j in d:
            temp_list = 0
            for ii in range(v):
                if v == 60:
                    if ii < 6:
                        temp_list = temp_list + d[j][ii]
                        if ii == 5:
                            temp_list = temp_list/6
                    else:
                        #time_lists[ii - 6].append(d[j][ii])
                        time_lists[ii-6].append(d[j][ii] - temp_list)
                else:
                    if len(d[j]) != 10:
                        print(cat + "has been skipped")     # Fehlerkontrolle
                        print(j)
                        print(d)
                        continue
                    else:

                        time_lists[ii].append(d[j][ii]) #sortieren in die einzelnen Gruppen nach Phasen

        if cat == 'meanNN':
            extender()


        #    print(ss.rankdata(d[j]))
        stati = ss.friedmanchisquare(*time_lists)        #durchführung Friedman-test


        if stati[1] < 0.1:                                                    #check auf relevanz
            print('...................................................................................................')
            print(stati)
            print("...................................................................................................")
            temp = []
            for jj in time_lists[1:]:
                print(ss.shapiro(jj))
                print(ss.wilcoxon(time_lists[0], jj))
        else:
            print(stati)

plt.show()
