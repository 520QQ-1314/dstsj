def critic_agent(state):
    res = llm.invoke(f"""
Score prompt 1-10.

Return JSON:
score + feedback

Prompt:
{state['prompt']}
""")
    return json.loads(res.content)
