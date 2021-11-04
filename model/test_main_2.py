import sys, os
from model.OCRModel import OCRModel

# 상위 경로(Project/)를 system PATH에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    ocrModel = OCRModel()

    # 여러개의 파일
    file_names = os.listdir("./data/available_image/ElectricityMeter")  # 이미지 파일 이름
    file_names.sort(reverse=False)
    print(file_names)
    for file_name in file_names:
        ocrModel = OCRModel()
        # roi 개수, 인식한 전력량계 제조번호
        result_roi, sava_images, serial_cd = ocrModel.get_roi_images("./data/available_image/ElectricityMeter", file_name)