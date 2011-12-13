clear
clc

addpath('C:\NXT\matlab_legonxt');


nxt = legoNXT('COM12');
nxti = nxtInterface('COM12', 2, 2);

c = clock; 
duration  = 4; 
i=0;

ultrasonic = nxt.Port4;
set(nxt.Port4, 'type', 'distance');
light = nxt.Port3;
set(nxt.Port2, 'type', 'light');
Lmotor = nxt.PortB;
Rmotor = nxt.PortC;
Arm = nxt.PortA;

start(Lmotor, 20);
start(Rmotor, 20);
dataSet = [];
dataLight = [];
while (etime (clock, c) < duration)
    %get data
    dataD = getdata(nxt.Port4)
    dataL = getdata(nxt.Port3)
    dataSet = [dataSet; dataD];
    dataLight = [dataLight; dataL];

    
    if (dataD > 260)
        stop(Lmotor);
        stop(Rmotor);
        pause(1);
        start(Lmotor, -20);
        pause(2.5);
        stop(Lmotor);
        stop(Rmotor);
    else if (dataL < 70)
        stop(Lmotor);
        stop(Rmotor);
        start(Arm, 25);
        pause(.3);
        stop(Arm);
        pause(.2);
        start(Arm, -25);
        pause(.2);
        stop(Arm);
        pause(1);
    else
        start(Lmotor, 30);
        start(Rmotor, 30);
    end
    end
    
    i = i + 1;
end


totalD = 0;
totalS = 0;
size = length(dataSet);
for (j=1 : size)
    totalD = totalD + dataSet(j);
    totalS = totalS + dataLight(j);
end


avgDist = totalD / size
avgLight = totalS / size

%display(nxt.Port4);
%display(nxt.PortB);

i = [1:length(dataSet)];



 %plot
plot(i, dataSet, '-b');
hold on;
plot(i, dataLight, '-r');
axis([0 size 0 1100]);
stop(Lmotor);
stop(Rmotor);