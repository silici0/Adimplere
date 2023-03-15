from src import asgi

app = asgi.create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
