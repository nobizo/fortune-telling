import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# サイドバーに12の星座のボタンを配置します。
st.sidebar.markdown('**星座を選択してください**')
selected_zodiac = st.sidebar.selectbox('星座を選択してください', ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座'])

# サイドバーの星座のボタンのどれか1つをクリックするとOpenAIのAPIにクリックした星座を渡し、OpenAIから今日の運勢を返してもらいます。
if selected_zodiac:
    st.write(f"{selected_zodiac}の運勢です")
    response = openai.Completion.create(
        engine="gpt-4",
        messages=[
            {"role": "system", "content": "You are a fortune teller."},
            {"role": "user", "content": f"今日の{zodiac}の運勢を教えてください。"}
        ]
    )

    bot_message = response.choices[0].text.strip()
    st.write(bot_message)
