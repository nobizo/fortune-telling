import streamlit as st
import openai

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
st.sidebar.markdown('**星座を選択してください**')
selected_zodiac = st.sidebar.selectbox('星座を選択してください', ['','牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座'])

# サイドバーの星座のボタンのどれか1つをクリックするとOpenAIのAPIにクリックした星座を渡し、OpenAIから今日の運勢を返してもらいます。
st.image("astrologer.png")
if selected_zodiac == "":
    st.write("星座を選んでください")
else:
    st.write(f"{selected_zodiac}の運勢です")
    
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
