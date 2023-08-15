import streamlit as st
import openai

# サイドバーに12の星座のボタンを配置します。
st.sidebar.markdown('**星座を選択してください**')
for zodiac in ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座']:
    st.sidebar.button(zodiac)

# サイドバーの星座のボタンのどれか1つをクリックするとOpenAIのAPIにクリックした星座を渡し、OpenAIから今日の運勢を返してもらいます。
zodiac = st.sidebar.selectbox('星座を選択してください', ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座'])
if zodiac:
    # OpenAIから今日の運勢を取得します。
    response = openai.create_response(
        engine='davinci',
        prompt='今日の運勢を教えてください。',
        temperature=0.7,
        top_p=0.9,
        presence_penalty=0.2,
        stop_token='。'
    )

    # OpenAIから返却されたテキストに含まれる今日の運勢のラッキーカラーをラッキーカラーフィールドに表示します。
    lucky_color = response.choices[0].text.split('。')[0].split('今日の運勢は')[1].split('です。')[0]
    st.write('ラッキーカラーは、' + lucky_color + 'です。')
