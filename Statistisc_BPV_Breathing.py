import scipy.stats as ss

for mes in ['BPV', 'Freq', 'Freq_per_Beat']: #loope duch BPV und Atmungs Parameter
    time_lists = [[] for _ in range(10)]
    for i in range(10):                      #loope durch Testpersonen
        filename = 'Pa' + str(i + 1) + '.txt/' + mes
        with open(filename, 'r') as file:     #Daten auslesen
            ii = 0  
            for line in file:                
                if ii > 9:
                    continue
                time_lists[ii].append(float(line))
                ii += 1

    stati = (ss.friedmanchisquare(*time_lists)) #friedman-Test wird durchgrführt
    if stati[1] < 0.1: #unterscheidung ob signifikant
        print('...................................................................................................')
        print(stati)
        print("...................................................................................................")
        temp = []
        for jj in time_lists[1:]:

            print(ss.wilcoxon(time_lists[0], jj))
    else:
        print(stati)
