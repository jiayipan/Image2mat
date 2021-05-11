imgPath = '/Users/xxx/Documents/yyy/';        % 图像库路径
imgDir  = dir([imgPath '*.png']); % 遍历所有jpg格式文件

for i = 1:length(imgDir)          % 遍历结构体就可以一一处理图片了
    img = imread([imgPath imgDir(i).name]); %读取每张图片
    gray = rgb2gray(img);
    temp3 = double(gray) / 255;
    a = ['/Users/xxx/Documents/yyy/(', int2str(i), ').mat'];
    save(a, 'temp3');
    fprintf('done\n');
end
