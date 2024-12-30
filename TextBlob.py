from textblob import TextBlob

# 使用者輸入文字
text = input("請輸入一句話：")

# 分析情感
blob = TextBlob(text)
polarity = blob.sentiment.polarity  # 情感極性 (-1 負面, 1 正面)
subjectivity = blob.sentiment.subjectivity  # 主觀性 (0 ~ 1)

# 判斷情感類別
if polarity > 0:
    print("這是一個正面的句子！")
elif polarity < 0:
    print("這是一個負面的句子！")
else:
    print("這是一個中立的句子！")

# 顯示詳細結果
print(f"情感極性：{polarity}")
print(f"主觀性：{subjectivity}")
