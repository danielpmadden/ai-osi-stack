from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.aeip_router import router as aeip_router
from .routers.ledger_router import router as ledger_router
from .routers.feedback_router import router as feedback_router

app = FastAPI(title="AI OSI Stack Governance Control Tower API")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(aeip_router, prefix="/api")
app.include_router(ledger_router, prefix="/api")
app.include_router(feedback_router, prefix="/api")


@app.get('/health')
def health_check():
  return {"status": "ok"}
