import streamlit as st
import openai
from datetime import datetime

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
私は非常によく当たる有名な星占い師です。ユーザーの星座を聞くと、次の出力形式で星占いの結果を返します。
【今日のラッキーカラー】と【ラッキーナンバー】をもとに今日の運勢がよくなるおすすめの【ランチのジャンル】をリコメンドしてください。
そして、【ランチのジャンル】をもとに具体的に【今日のラッキーランチ】をレコメンドしてください。
【ランチのジャンル】は# ランチジャンルから1つ選択すること。
# 出力形式
【今日の運勢】
【今日のラッキーカラー】
【今日のラッキーナンバー】
【ランチのジャンル】
【今日のラッキーランチ】
# ランチジャンル
1. 中華料理屋
2. ラーメン店
3. カレーショップ
4. 牛丼屋
5. ハンバーガーショップ
6. 天ぷら屋
7. 洋食（ステーキ・ハンバーグ・コロッケ・生姜焼き）
8. とんかつ
9. から揚げ
10. 和食（刺身、焼き魚、肉じゃが）
11. 寿司屋
12. ハワイアン
13. イタリアン
14. タイ料理
15. インド料理
16. アジア料理
"""

# サイドバーに12の星座のボタンを配置します。
# st.sidebar.markdown('**星座を選択してください**')
# selected_zodiac = st.sidebar.selectbox('星座を選択してください', ['','牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座'])

# サイドバーに生年月日の入力フィールドを配置します。
st.sidebar.markdown('**生年月日を入力してください**')

# 選択可能な日付範囲を指定して date_input を使用します。
min_date = datetime(1962, 1, 1)
max_date = datetime(2030, 12, 31)
birth_date = st.sidebar.date_input('生年月日', min_value=min_date, max_value=max_date)
birth_year = birth_date.year

# 生年月日から星座を計算する関数
def calculate_zodiac(birth_date):
    zodiacs = ['山羊座', '水瓶座', '魚座', '牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座']
    day_month = birth_date.strftime('%m%d')
    
    if (day_month >= '1222' or day_month <= '0119'):
        return zodiacs[0]  # 山羊座
    elif (day_month >= '0120' and day_month <= '0218'):
        return zodiacs[1]  # 水瓶座
    elif (day_month >= '0219' and day_month <= '0320'):
        return zodiacs[2]  # 魚座
    elif (day_month >= '0321' and day_month <= '0419'):
        return zodiacs[3]  # 牡羊座
    elif (day_month >= '0420' and day_month <= '0520'):
        return zodiacs[4]  # 牡牛座
    elif (day_month >= '0521' and day_month <= '0620'):
        return zodiacs[5]  # 双子座
    elif (day_month >= '0621' and day_month <= '0722'):
        return zodiacs[6]  # 蟹座
    elif (day_month >= '0723' and day_month <= '0822'):
        return zodiacs[7]  # 獅子座
    elif (day_month >= '0823' and day_month <= '0922'):
        return zodiacs[8]  # 乙女座
    elif (day_month >= '0923' and day_month <= '1022'):
        return zodiacs[9]  # 天秤座
    elif (day_month >= '1023' and day_month <= '1121'):
        return zodiacs[10]  # 蠍座
    else:
        return zodiacs[11]  # 射手座


# 生年月日から星座を計算
selected_zodiac = ""
if birth_date:
    birth_year = birth_date.year
    selected_zodiac = calculate_zodiac(birth_date)


# サイドバーの星座のボタンのどれか1つをクリックするとOpenAIのAPIにクリックした星座を渡し、OpenAIから今日の運勢を返してもらいます。
st.image("astrologer.png")
if selected_zodiac == "":
    st.write("星座を選んでください")
else:
    st.write(f"{birth_year}年生まれの{selected_zodiac}の運勢です")
    
    user_message = f"今日の{selected_zodiac}の運勢を教えてください。"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    bot_message = response.choices[0].message['content']
    st.write(bot_message)
