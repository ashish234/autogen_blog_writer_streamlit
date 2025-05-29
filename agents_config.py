from autogen import AssistantAgent, UserProxyAgent

writer = AssistantAgent(
    name="WriterAgent",
    system_message="You are a professional blog writer. Write a blog post of ~500 words on the given topic in a clear and engaging tone."
)

seo = AssistantAgent(
    name="SEOAgent",
    system_message="""
You are an SEO specialist. Review the given blog post for:
1. Target keyword usage
2. Meta description quality
3. Heading structure (H1, H2s)
4. Readability and tone
5. Suggestions for improving search engine ranking.
"""
)

editor = AssistantAgent(
    name="EditorAgent",
    system_message="You are a blog editor. Improve the blog post using the SEOAgent's feedback. Keep it human-readable and engaging."
)

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="TERMINATE",
    code_execution_config=False,
)
