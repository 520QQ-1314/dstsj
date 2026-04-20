def style_agent(state):
    res = llm.invoke(f"""
Define visual style JSON.

Concept:
{state['concept']}
""")
    return {"style": json.loads(res.content)}
