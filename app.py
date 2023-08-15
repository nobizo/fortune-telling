import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# サイドバーに12の星座のボタンを配置します。
st.sidebar.markdown('**星座を選択してください**')
for zodiac in ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座']:
    st.sidebar.button(zodiac)

# サイドバーの星座のボタンのどれか1つをクリックするとOpenAIのAPIにクリックした星座を渡し、OpenAIから今日の運勢を返してもらいます。
zodiac = st.sidebar.selectbox('星座を選択してください', ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座'])
if zodiac:
    # OpenAIから今日の運勢を取得します。
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages='今日の運勢を教えてください。'
    )

    # OpenAIから返却されたテキストに含まれる今日の運勢のラッキーカラーをラッキーカラーフィールドに表示します。
    lucky_color = response.choices[0].text.split('。')[0].split('今日の運勢は')[1].split('です。')[0]
    st.write('ラッキーカラーは、' + lucky_color + 'です。')
