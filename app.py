import streamlit as st
from textblob import TextBlob

# 應用標題
st.title("情感分析工具")

# 使用者輸入文字
text = st.text_area("請輸入文字：")

# 按下按鈕執行情感分析
if st.button("分析情感"):
    if text.strip():  # 確保有輸入文字
        # 分析情感
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # 情感極性 (-1 負面, 1 正面)
        subjectivity = blob.sentiment.subjectivity  # 主觀性 (0 ~ 1)

        # 判斷情感類別
        if polarity > 0:
            st.write("### 這是一個正面的句子！")
        elif polarity < 0:
            st.write("### 這是一個負面的句子！")
        else:
            st.write("### 這是一個中立的句子！")

        # 顯示詳細數據
        st.write(f"- **情感極性 (Polarity)**：{polarity:.2f}")
        st.write(f"- **主觀性 (Subjectivity)**：{subjectivity:.2f}")
    else:
        st.write("⚠️ **請輸入文字再按下按鈕！**")
