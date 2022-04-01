import img_send
import seg_send
import re

boxCount_keyowrds = ["箱數：", "箱敷"]
threshold = 4


# return number of chinese words
def hans_count(str):
    hans_total = 0
    for s in str:
        if '\u4e00' <= s <= '\u9fef':
            hans_total += 1
    return hans_total


def get_product_NameCount_pair(ocr_results):
    """
    1.輸入ocr的結果List format
    2.確認中文字的字數是否大於threshold
    3.確認是否包含預先定義的關鍵字
    4.產生可能包含商品名稱或數量的candidate_list
    5.由candidate_list找出商品名稱與箱數的配對
    """
    candidate_list = []
    for elm in ocr_results:
        # step2 中文字長度檢查
        if hans_count(elm) > threshold:
            candidate_list.append(elm)
        # step3 中文字關鍵字檢查
        for keyword in boxCount_keyowrds:
            if keyword in elm:
                candidate_list.append(elm)
    # step4 產生可能包含商品名稱或數量的candidate_list
    print(candidate_list)
    boxCount_list = []
    pre_productName = ""
    rule = re.compile(r"：\d", re.U) #判斷"："後是否是數字
    # step5 產生可能包含商品名稱或數量的candidate_list
    for elm in candidate_list:
        if "：" in elm:
            num = ''.join([x for x in elm if x.isdigit()])
            # print(pre_productName+","+num)
            if num == "" or pre_productName == "":
                continue
            if rule.search(elm) is None: #"："後如果不是數字就continue
                continue
            pair = [pre_productName, num]
            boxCount_list.append(pair)
            continue
        pre_productName = elm
    return boxCount_list


if __name__ == '__main__':
    # img_path = './img/Carrefour/2545314538.jpg'
    # img_path = './img/Carrefour/2545314541.jpg'
    img_path = './img/Carrefour/2545314544.jpg'
    # img_path = './img/Carrefour/crop.jpg'
    ocr_server_IP = "192.168.50.29:6000"
    show_ocr_pic = True
    ocr_results = img_send.ocr(img_path, ocr_server_IP, show_ocr_pic)
    print(ocr_results)
    boxCount_list = get_product_NameCount_pair(ocr_results)
    print(boxCount_list)


