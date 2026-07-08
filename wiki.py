import wikipedia

wikipedia.set_user_agent("MyPythonApp/1.0 (https://example.com; test@example.com)")

print(wikipedia.summary("Star Wars", sentences=2, auto_suggest=False))