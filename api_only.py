import uvicorn

# Runs the FastAPI server ONLY.

uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)

# So apparently this fundciton isn't working..., so just run this command
# python -m uvicorn api.main:app --reload
