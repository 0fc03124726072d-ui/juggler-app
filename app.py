import streamlit as st
import time

# リール配列
REEL = ["ぶどう", "サイ", "ぶどう", "BAR", "チェリー", "サイ", "ぶどう", "サイ", "ピエロ", "7", "ぶどう", "サイ", "チェリー", "BAR", "ぶどう", "サイ", "ぶどう", "サイ", "7", "ベル", "ベル"]

st.title("ビタ押し練習機")

# 1周0.78秒なので、1コマあたりの秒数を計算
time_per_frame = 0.78 / 21

# 現在の経過時間から位置を計算
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

elapsed = time.time() - st.session_state.start_time
pos = int((elapsed / time_per_frame)) % 21

st.subheader(f"現在の枠内: {REEL[pos]}")

if st.button("ビタ止め！"):
    st.write(f"結果: {REEL[pos]} で止まりました！")
else:
    # リアルタイムで回転させる
    time.sleep(0.01)
    st.rerun()
