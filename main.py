from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import health, upload, analyze

app = FastAPI(
    title="ATS CV Scanner API",
    description="Simple ATS CV Scanner with keyword matching",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(upload.router, tags=["Upload"])
app.include_router(analyze.router, tags=["Analyze"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)