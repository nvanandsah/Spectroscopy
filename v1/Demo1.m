x = imread("Combinational White light.jpeg");
rgbValues = spectrumRGB(400:0.2:650);
image = repmat(rgbValues, 200, 1, 1);
imshow(image)