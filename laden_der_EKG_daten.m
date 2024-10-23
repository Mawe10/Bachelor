fileName = load('Pa1.mat');
C = fieldnames(fileName);
ECG = fileName.BeatToBeat.RR;
j = 1;
big = size(ECG);
data = [];
strt = 'trash';
fid = fopen(strt,'wt');
myfolder = 'Pa1';
mkdir(myfolder);
cd(myfolder);
while big(1) + 1 > j
    j
    if j == 1
        p = 1;
    else 
        if j == 2
            myfolder = 'Pa1base';
            mkdir(myfolder);
            cd(myfolder);
        else
            myfolder = 'Pa1Ph';
            myfolder = [myfolder, num2str(j - 2)];
            mkdir(myfolder);
            cd(myfolder)
        end
    end
    
    ECG_current = ECG(j);
    bob = cell2mat(ECG_current);
    limiter = floor(size(bob, 2) / 6);
    for counter = 1:6
        strt = num2str(counter);
        fid = fopen(strt,'wt');
        limit =(limiter * counter);
        for i = bob(1, 1 + limit-limiter:limit)
            data(end + 1) = i;
        end
        bob_now = bob(1 + limit-limiter:limit);
        for i = 1:length(bob_now)
            fprintf(fid, '%f\r\n', bob_now(1, i));
        end
    end
    if j > 1
        cd('..');
    end
    j = j + 1;
end
cd('..');
