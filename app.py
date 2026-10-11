import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("Atras_bot")

st.write("##### アトラスキャラなりきりボット")

selected_item = st.radio(
    "エージェントを選択してください",
    ["桐生一馬", "雨宮蓮"]
)

st.divider()

if selected_item == "桐生一馬":
    st.write("桐生さんが人生の相談に乗ってくれます")
    #systemlogをセット
    systemMessage = "あなたは東條会元4代目の伝説的な極道であり、今は堅気です。豊富な経験から、ユーザの人生相談に乗ってください。口数は少ないですが、人情深い性格で、口癖は「なんだ」「死にてえやつだけかかってこい」語尾はぜ。だ。など"

elif selected_item == "雨宮蓮":
    st.write("蓮がお勧めのコーヒーを提案してくれます")
    #systemlogをセット
    systemMessage = "あなたはコーヒー専門店の屋根裏で生活する雨宮蓮です。いつもマスターの仕事を見ておりコーヒーには詳しく、ユーザの気分屋要望に対して、ブルーマウンテンやキリマンジャロなどコーヒーの提案を行ってください。優しい兄貴的な存在で、語尾は「だ。」「~だからな」など"

input_message = st.text_input(label="質問文を書いていください。")

if st.button("実行"):
    st.divider()

    if input_message:
        messages = [
            SystemMessage(content=systemMessage),
            HumanMessage(content=input_message),
        ]
        result = llm.invoke(messages)
        st.write(result.content)

    else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")
