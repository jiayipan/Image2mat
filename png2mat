import glob
import numpy as np
from PIL import Image
import scipy.io as io
import torchvision.transforms as transforms

src_dir = '/Users/xxx/Documents/数据集/URBAN100_PNG/'
save_dir = '/Users/xxx/Documents/数据集/URBAN100_MAT'
file_list = glob.glob(src_dir+'*.png')
image_transforms = transforms.Compose([transforms.ToTensor(), transforms.Grayscale(1)])
print('Start...')

for i in range(file_list.__len__()):
    img = Image.open(file_list[i])
    res = image_transforms(img)
    res = np.array(res, dtype=np.float32) / 255
    io.savemat(save_dir + '/({}).mat'.format(i + 1), {'temp3': res})
print('done')
