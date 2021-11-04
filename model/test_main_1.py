import sys, os
from model.OCRModel import OCRModel

# 상위 경로(Project/)를 system PATH에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    ocrModel = OCRModel()

    # 파일 1개 읽을 때 사용
    filename = "01232004273_P1163.jpg"
    result_roi, sava_images, serial_cd = ocrModel.get_roi_images('../static/img', filename)