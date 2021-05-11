import glob
import numpy as np
import scipy.io as io
import torchvision
from PIL import Image

src_dir = '/Users/xxx/Documents/数据集/URBAN100_PNG/'
save_dir = '/Users/xxx/Documents/数据集/URBAN100_MAT'
file_list = glob.glob(src_dir+'*.png')
print('Start...')

for i in range(file_list.__len__()):
    img = Image.open(file_list[i])

    img = torchvision.transforms.ToTensor()(img)
    img = torchvision.transforms.Grayscale(num_output_channels=1)(img).squeeze()
    img = img.numpy()
    io.savemat(save_dir + '/({}).mat'.format(i + 1), {'temp3': img})
print('done')
