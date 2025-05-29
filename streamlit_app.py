import streamlit as st
from autogen import GroupChat, GroupChatManager
from agents_config import user_proxy, writer, seo, editor

st.title("📝 Blog Writer with SEO Agent")

topic = st.text_input("Enter a blog topic", value="Top 5 AI Security Trends in 2025")

if st.button("Generate Blog Post"):
    with st.spinner("Generating blog post using AutoGen agents..."):
        group_chat = GroupChat(agents=[user_proxy, writer, seo, editor], messages=[], max_round=10)
        manager = GroupChatManager(groupchat=group_chat, admin_agent=user_proxy)
        chat_result = manager.initiate_chat(message=f"Please write a blog post on: {topic}")

        st.success("Blog generation complete.")
        for msg in chat_result.chat_history:
            st.markdown(f"**{msg['name']}**: {msg['content']}")
