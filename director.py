def director_agent(state):
    res = llm.invoke(f"""
You are an art director.

Create creative direction JSON.

Intent:
{state['intent']}
""")
    return {"concept": json.loads(res.content)}
