%multiBit Kanha Code
clear all;
clc;
close all;

%% Transmission Parameters

%number of bits possible in one frame
bits = 3;

a = arduino();
code = '000001010011100101110111';

i = 1;

while(i<(length(code)-bits))
	if (code(i:i+bits-1) == '000')
	    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',0);
		disp("000");
		end
	if (code(i:i+bits-1) == '001')
	    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',5);
		disp("001");
		end
	if (code(i:i+bits-1) == '010')
	    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',0);
		disp("010");
		end
	if (code(i:i+bits-1) == '011')
	    writePWMVoltage(a,'D9',0);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',5);
		disp("011");
		end
	if (code(i:i+bits-1) == '100')
	    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',0);
		disp("100");
		end
	if (code(i:i+bits-1) == '101')
	    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',0);writePWMVoltage(a,'D11',5);
		disp("101");
		end
	if (code(i:i+bits-1) == '110')
	    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',0);
		disp("110");
		end
	if (code(i:i+bits-1) == '111')
	    writePWMVoltage(a,'D9',5);writePWMVoltage(a,'D10',5);writePWMVoltage(a,'D11',5);
		disp("111");
		end
		i = i+bits;
end


%% Receiver Parameters Considering only images NOT REALTIME

j = 1;
while(j<(2^bits+1))
	name = (['image',num2str(j),'.jpg']); 
	img = imread(name);
	subplot(4,2,j);
	j=j+1;
    [yRed, x]=imhist(img(:,:,1));
    [yGreen, x]=imhist(img(:,:,2));
    [yBlue, x]=imhist(img(:,:,3));
end