global map
global map_x
global map_y

map = zeros(1000,1000);

Build_Map_highrez()

map = map';

map_x = zeros(1000,1000);
map_y = zeros(1000,1000);


force = 50;
field = 30;

for i = field+1: 1 :1000-field
    for j = field+1: 1 :1000-field
        if map(i,j) == 1
            map_x(j, i) = force;
            map_y(j, i) = force;
            i
            j           

            for ii = -field:field
                for jj = -field:field
                    
                    if map_x(j, i+ii) == 0
%                         map_x(j, i+ii) = ii*force/abs(ii);                        
                        map_x(j, i+ii) = ii*force/abs(ii)-ii*force/field;
                    end
                    
                    if map_y(j+jj, i) == 0
%                         map_y(j+jj, i) = jj*force/abs(jj);
                        map_y(j+jj, i) = jj*force/abs(jj)-jj*force/field;                        
                    end
                end
            end
        end
    end
end

% for i = 1:100
%     for j = 1:100
% figure(3)
% plot(map_x(:,100), map_y(:,100)); hold on
% axis([0 100 0 100])
% 
% figure(4)
% plot(map_y); hold on
% axis([0 100 0 100])
map = map';

figure(5);
for i = 1:1000
    for j = 1:1000
        if map(i,j) > 0
            plot(i, j, 'ob'); hold on;
        end
        
        if map_x(i,j) > 0
            plot(i,j, 'dr'); hold on;
        end
        
        if map_x(i,j) < 0
            plot(i,j, 'dy'); hold on;
        end

        if map_y(i,j) > 0
            plot(i,j, 'xc'); hold on;
        end
        
        if map_y(i,j) < 0
            plot(i,j, 'xg'); hold on;
        end        
        
    end
end
axis([0 1000 0 1000]);