def prompt_agent(state):
    res = llm.invoke(f"""
Convert into ONE image prompt.

No JSON.

Intent: {state['intent']}
Concept: {state['concept']}
Layout: {state['layout']}
Style: {state['style']}
""")
    return {"prompt": res.content}
