for j = 1:10
    folders = {'Pa1.txt', 'Pa2.txt', 'Pa3.txt', 'Pa4.txt', 'Pa5.txt', 'Pa6.txt', 'Pa7.txt', 'Pa8.txt', 'Pa9.txt', 'Pa10.txt'};           %Erstellen der Ordner zum speichern
    myfolder = folders{j};
    mkdir(myfolder);
    cd(myfolder);
    names = {'Pa1.mat', 'Pa2.mat', 'Pa3.mat', 'Pa4.mat', 'Pa5.mat', 'Pa6.mat', 'Pa7.mat', 'Pa8.mat', 'Pa9.mat', 'Pa10.mat'}              %Auslesen der Daten 
    fileName = load(names{j});
    HR = fileName.BeatMeanStat.HR;
    FreqBreath = fileName.BeatMeanStat.FreqBreath;                                                                                       
    BPV = fileName.BPVStatistics.RATIO                                                
    sz = size(HR);
    sz = sz(1);
    strt = 'Freq';
    fid = fopen(strt,'wt');
    for i = 2:sz
        fprintf(fid, '%f\r\n', FreqBreath{i}.Mean);                        
    end
    strt = 'Freq_per_Beat';
    fid = fopen(strt,'wt');
    for i = 2:sz
        stat = FreqBreath{i}.Mean/HR{i}.Mean;
        fprintf(fid, '%f\r\n', stat);
    end
    strt = 'BPV';
    fid = fopen(strt,'wt');
    for i = 2:sz
        stat = BPV{i}.Mean;
        fprintf(fid, '%f\r\n', stat);
    end
    cd('..')
end
