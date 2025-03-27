import numpy as np
import cv2

# 生成一张512*512的纯黑色背景图片
black_image = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.imwrite('black_background.png', black_image)


