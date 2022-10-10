clear all
close all
clear variables
samplefreq = 250;
T = readtable('rightleft');
%delete start up values
T([1:400],:) = [];
data = normalize(T.EXGChannel2, 'zscore');
data1= normalize(T.EXGChannel3,'zscore');
data2=normalize(T.EXGChannel5,'zscore');
data3=normalize(T.EXGChannel6,'zscore');

%data = lowpass(T.EXGChannel4,62,250);
timedata = T.Timestamp_Formatted_;
pointsize= 400;
points = length(data)/pointsize;


datapointlistleft = [];
datapointlistleft1 = [];
datapointlistright = [];
datapointlistright1 = [];
blueminusredlist=[];
blueminusredlist1=[];
timelist=[];
zerolist=[];
for n = 0:points-1
    zerolist=[zerolist 0];

    x=data(((n*pointsize)+1):((n+1)*pointsize));
    x1=data1(((n*pointsize)+1):((n+1)*pointsize));
    x2=data2(((n*pointsize)+1):((n+1)*pointsize));
    x3=data3(((n*pointsize)+1):((n+1)*pointsize));
    
    datapointleft = rms(x2);
    datapointleft1 = rms(x3);
    datapointright = rms(x);
    datapointright1 = rms(x1);
    
    blueredpoint = datapointleft-datapointright;
    blueredpoint1 = datapointleft1-datapointright1;
    timepoint =timedata((n+1)*pointsize);

    timelist=[timelist timepoint];
    datapointlistleft=[datapointlistleft datapointleft];
    datapointlistleft1=[datapointlistleft1 datapointleft1];
    datapointlistright = [datapointlistright datapointright];
    datapointlistright1 = [datapointlistright1 datapointright1];
    blueminusredlist = [blueminusredlist blueredpoint];
    blueminusredlist1 = [blueminusredlist1 blueredpoint1];
end
%events
events=[];
for i=0:15*samplefreq
    events=[events 0];
end
for j = 0:1
    for i=0:30*samplefreq
        events=[events -0.5];
    end
    for i=0:15*samplefreq
        events=[events 0.0];
    end
    for i=0:30*samplefreq
        events=[events 0.2];
    end
    for i=0:15*samplefreq
        events=[events 0.0];
    end
end
diff=length(timedata)-length(events)
for i=0:diff-1
        events=[events 0];
end

% %for the file Rida messed up
% for i=0:30*samplefreq
%         events=[events -5];
%     end
%     for i=0:15*samplefreq
%         events=[events 0];
%     end
%     for i=0:30*samplefreq
%         events=[events 5];
%     end
%     for i=0:30*samplefreq
%         events=[events 0];
%     end
%  
%  for i=0:30*samplefreq
%         events=[events -5];
%     end
%     for i=0:15*samplefreq
%         events=[events 0];
%     end
%     for i=0:30*samplefreq
%         events=[events 5];
%     end
%     for i=0:15*samplefreq
%         events=[events 0];
%     end
%  for i=0:30*samplefreq
%         events=[events -5];
%     end
%     for i=0:15*samplefreq
%         events=[events 0];
%     end
%     for i=0:30*samplefreq
%         events=[events 5];
%     end
%    
%     
%  
% diff=length(timedata)-length(events)
% for i=0:diff-1
%         events=[events 0];
% end
% N= length(data);
figure
plot(timelist,blueminusredlist, 'LineWidth',2);
hold on
x=plot(timelist,datapointlistleft,'LineWidth',0.5, 'LineStyle','-.');

plot(timelist,datapointlistright, 'LineWidth',0.5, 'LineStyle','-.');

%plot(timelist,blueminusredlist1);
plot(timedata,events)
plot(timelist,zerolist);

legend("DIFFERENCE","RIGHT","LEFT","BENCHMARK(-0.5 = Left, 0.2 = Right)","ZERO")
xlabel('Time')
ylabel('Normalised (Z-Score) RMS Voltage (V)')
grid;
title('Left hand versus right hand EEG response')
