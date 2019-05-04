close all;
clear all;
clc
a = arduino();
code = "000001010011100101110111";
s = strlength(code);
code = split(code,"");
% cam = webcam;
  
writePWMVoltage(a,'D9',0);
% background = snapshot(cam);
cred = [];
cgreen = [];
i = 0;
imgarr = [];
url = "http://192.168.161.33:8080/shot.jpg";
tic;
while(i<10)
%   c2 = [];
%   c3 = [];
   imgc = [];
%  j = 1;
  pause(0.1);
  for index = 2:3:s
        if(code(index)=='1')
            if(code(index+1)=='1')
                if(code(index+2)=='1')
                    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',5);
                    disp("111");
                else
                    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',0);
                    disp("110");
                end
            else
                if(code(index+2)=='1')
                    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',5);
                    disp("101");
                else
                    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',0);
                    disp("100");
                end
            end
        else
            if(code(index+1)=='1')
                if(code(index+2)=='1')
                    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',5);
                    disp("011");
                else
                    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',0);
                    disp("010");
                end
            else
                if(code(index+2)=='1')
                    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',5);
                    disp("001");
                else
                    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',0);
                    disp("000");
                end
            end
        end
        
        pause(0.3);
        img = imread(url);
%         img = snapshot(cam);
        
%         subplot(4,2,j);
%         j=j+1;
%         [yRed, x]=imhist(img(:,:,1));
%         [yGreen, x]=imhist(img(:,:,2));
%         [yBlue, x]=imhist(img(:,:,3));
%         disp((yRed(length(yRed))))
%         plot(x, yRed, 'Red', x, yGreen, 'Green', x, yBlue, 'Blue');
%         xlim([5 250])
%         c2 = [c2 yRed(length(yRed))];
%         c3 = [c3 yGreen(length(yGreen))];
%         imshow(rgb2gray(img));
%         hist(reshape(img,[],3),1:max(img(:)));
%         colormap([1 0 0;0 1 0;0 0 1]);
       imgc = [imgc img];
        pause(0.2);
   %     
  end
  imgarr = [imgarr; imgc];
   i = i+1
%   cred = [cred; c2];
%   cgreen = [cgreen; c3];
end
toc;