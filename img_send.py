# pip install requests
# pip install opencv-python
# pip install opencv-contrib-python #optional

import requests
import time
import base64
import cv2
import numpy as np


def Json_converImgtoBase64(img_file_path):
    img = cv2.imread(img_file_path)
    string = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
    return string


def Json_converBase64toImg(img_b64encode, img_file_path, isShow):
    jpg_original = base64.b64decode(img_b64encode)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    cv2.imwrite(img_file_path, img)
    if isShow:
        cv2.imshow("img", img)
        cv2.waitKey()


def ocr(img_path, server_IP, show_ocr_pic):
    # create b64code image file to json
    img_b64code = Json_converImgtoBase64(img_path)
    sendMessage_json = {
        "image": img_b64code
    }
    # sent json to server
    res = requests.post('http://' + server_IP + '/getResult', json=sendMessage_json)
    # res = requests.post('http://test.ipickup.com.tw:15000/getResult', json=sendMessage_json)

    # output
    img_output_path = "./OCR_result_img.jpg"
    if res.ok:
        outputs = res.json()
        #print(outputs['ocr_txt'])
        if show_ocr_pic:
            img_ocr_result_b64code = outputs['ocr_img_b64code']
            Json_converBase64toImg(img_ocr_result_b64code, img_output_path, False)
    else:
        print("OCR abnormal return, please have check")
    return outputs['ocr_txt']

if __name__ == '__main__':
    # img_path = './Carrefour/2545314538.jpg'
    # img_path = './Carrefour/2545314541.jpg'
    # img_path = './Carrefour/2545314544.jpg'
    img_path = './img/Carrefour/crop.jpg'

    # create b64code image file to json
    img_b64code = Json_converImgtoBase64(img_path)
    sendMessage_json = {
        "image": img_b64code
    }

    start = time.time()
    # sent json to server
    res = requests.post('http://192.168.50.29:6000/getResult', json=sendMessage_json)
    # res = requests.post('http://test.ipickup.com.tw:15000/getResult', json=sendMessage_json)

    # output
    img_output_path = "./OCR_result_img.jpg"
    if res.ok:
        outputs = res.json()
        img_ocr_result_b64code = outputs['ocr_img_b64code']
        Json_converBase64toImg(img_ocr_result_b64code, img_output_path, False)
        print(outputs['ocr_txt'])

    else:
        print("Abnormal return, please have check")
    end = time.time()
    print('time: ', end - start)
