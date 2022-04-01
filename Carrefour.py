import img_send
import seg_send

# ocr_results = ['行', '箱資訊', '箱/展', '“箱/板', 'PCB', '訂貨箱', '拒收原因', '商品代', '商品名稿', '訂單量', '收資訊', '號', 'SPCB', '長x真高，重量',
#                '數', '/板蛋量', '數量', '6', '一匙罐抗菌EX超縮洗粉', '總件敷：0', '37.00×35.00×17.00', '9.00 72.00', '1.8KG', '432', '72',
#                '11101039001', '總箱敷：72', '12.20', '8.00878.40', '1', 'A-018-0004-01', '公斤：0.00', '有效日期：2025-03-11', '6',
#                'Ex一匙囊抗菌洗衣精補', '總件敷：0', '30.00×25.00×28.00', '12.0072.00', '468', '1.5KG', '78', '11103021001', '總箱數：78',
#                '10.62', '2', '6.00764.64', 'A-019-0040-01', '人', '公斤：0.00', '有效日期：2025-02-15', '6', '一匙抗菌EX防洗褲',
#                '12.00 72.00', '總件數：0', '30.00×25.00×28.00', '1.5L', '11103317001', '468', '78', '錦箱數：78', '9.90', '1',
#                '6.00712.80', 'A-019-0183-01', '公斤：0.00', '有效日期：2025-03-072025-03-08']
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
    # print(candidate_list)
    boxCount_list = []
    pre_productName = ""
    # step5 產生可能包含商品名稱或數量的candidate_list
    for elm in candidate_list:
        if "：" in elm:
            num = ''.join([x for x in elm if x.isdigit()])
            # print(pre_productName+","+num)
            pair = [pre_productName, num]
            boxCount_list.append(pair)
            continue
        pre_productName = elm
    return boxCount_list


if __name__ == '__main__':
    img_path = './img/Carrefour/crop.jpg'
    ocr_server_IP = "192.168.50.29:6000"
    show_ocr_pic = True
    ocr_results = img_send.ocr(img_path, ocr_server_IP, show_ocr_pic)
    boxCount_list = get_product_NameCount_pair(ocr_results)
    print(boxCount_list)
