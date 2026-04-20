def layout_agent(state):
    res = llm.invoke(f"""
Define layout structure JSON.

Concept:
{state['concept']}
""")
    return {"layout": json.loads(res.content)}
