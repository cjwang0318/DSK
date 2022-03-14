from strsim.cosine import Cosine


def cosine(str1, str2):
    cosine = Cosine(2)
    p0 = cosine.get_profile(str1)
    p1 = cosine.get_profile(str2)
    score = cosine.similarity_profiles(p0, p1)
    return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Str1 = "妮维雅 Q10 Plus 美体 紧肤 乳液 400 ml"
    Str2 = "妮維雅 美體 緊膚 乳液 Q 10 plus 400 ml ( 新"
    Str3 = "妮維雅 美白 潤膚 乳液 400 ml"

    print(cosine(Str1, Str2))
    print(cosine(Str1, Str3))
    print("---------------------")

    Str1 = "妮維雅 美白 潤膚 乳液 400 ML + 深層 潤膚 乳液 125 ML ( 屈臣氏 美白 組合 包 )"
    Str2 = "妮維雅 美白 潤膚 乳液 組合 包"
    Str3 = "妮維雅 美白 潤膚 乳液 400 ml"
    print(cosine(Str1, Str2))
    print(cosine(Str1, Str3))
    print("---------------------")

    Str1 = "妮維雅 水潤 Q10 組 ( 深層 400 + 美 彈 125 ML ) WSN"
    Str2 = "妮維雅 水潤 Q10 組"
    Str3 = "妮維雅 極 淨 深層 眼部 卸妝液 125 ml"
    print(cosine(Str1, Str2))
    print(cosine(Str1, Str3))
