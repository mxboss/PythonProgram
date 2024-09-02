import cv2
import pytesseract

# 如果Tesseract未添加到系统路径中，需要指定tesseract.exe的路径
# pytesseract.pytesseract.tesseract_cmd = r'你的Tesseract安装路径\tesseract.exe'

# 读取图片
image = cv2.imread('doc.jpg')


# 将图片转换为灰度图像（可选）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 进行阈值处理（可选，可能有助于提高识别效果）
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 使用pytesseract提取文字
text = pytesseract.image_to_string(thresh)  # 如果是中文图片使用 'chi_sim'，英文可以省略

# 输出提取的文字
print("提取的文字：")
print(text)

# 显示图像（可选）
cv2.imshow('Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
