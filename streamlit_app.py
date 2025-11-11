import streamlit as st
from xai_sdk.client import Client  # FIXED LINE!

st.set_page_config(page_title="MumLife AI", layout="centered")

st.markdown("""
<style>
.big-font {font-size:50px !important; color:#FF69B4; font-weight:bold;}
.chat-message {padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem;}
.user {background-color: #FFE4E1;}
.assistant {background-color: #E6E6FA;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🎈 MumLife AI 👶</p>', unsafe_allow_html=True)
st.markdown("### British Mum Chaos? Grok-4 fixes it in 20 sec 💷")

if "messages" not in st.session_state:
    st.session_state.messages = []

client = Client(api_key=st.secrets["XAI_API_KEY"])

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your mum drama here... (e.g. Toddler meltdown in Tesco?)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.create(
            model="grok-4",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

st.markdown("---")
st.caption("Made with ❤️ by @Astrokeerthi | £19/month – 7-day free trial")
if st.button("Subscribe £19/month (cancel anytime)"):
    st.markdown("[Click here for Gumroad](https://gumroad.com/l/mumlifeai)")
