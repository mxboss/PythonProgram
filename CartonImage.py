import cv2
import numpy as np


def cartoonize_image(image):
    # 1. 读取图像
    img = cv2.imread(image)

    # 2. 转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. 使用中值滤波平滑图像
    gray = cv2.medianBlur(gray, 7)

    # 4. 检测边缘
    # 使用自适应阈值化来获取边缘
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

    # 5. 应用双边滤波来平滑图像，同时保留边缘
    color = cv2.bilateralFilter(img, 9, 75, 75)

    # 6. 将边缘图像与平滑图像合并
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


def cv_show(winname='Image', image=None):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winname, 800, 1000)
    cv2.imshow(winname, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 图像路径
input_image = 'yibo.png'
output_image = 'cartoonized_image.jpg'

# 执行卡通化处理
cartoon_image = cartoonize_image(input_image)

# 保存和显示结果
cv2.imwrite(output_image, cartoon_image)
# cv_show('oriImage', input_image)
cv_show('carton', cartoon_image)
