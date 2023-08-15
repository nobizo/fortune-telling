import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
私は非常によく当たる有名な星占い師です。ユーザーの星座を聞くと、次の出力形式で星占いの結果を返します。
今日のラッキーカラーとラッキーナンバーをもとに今日の運勢がよくなるおすすめのランチをリコメンドしてください。
# 出力形式
【今日の運勢】
【今日のラッキーカラー】
【今日のラッキーナンバー】
【今日のランチ】
"""

# サイドバーに12の星座のボタンを配置します。
st.sidebar.markdown('**星座を選択してください**')
selected_zodiac = st.sidebar.selectbox('星座を選択してください', ['','牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座'])

# サイドバーの星座のボタンのどれか1つをクリックするとOpenAIのAPIにクリックした星座を渡し、OpenAIから今日の運勢を返してもらいます。
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
