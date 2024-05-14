from fastapi import FastAPI
from .routes.lottery_routes import lottery_routes
from .routes.user_routes import user_routes
from .scripts.generate_lottery_number import generate_lottery_number
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore

app = FastAPI()

app.include_router(lottery_routes)
app.include_router(user_routes)

jobstores = {
    'default': MemoryJobStore()
}    
    
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='America/New_York') 

@scheduler.scheduled_job('interval', seconds=10)
def scheduled_job_1():
    generate_lottery_number()

@app.on_event("startup")
async def startup_event():
    scheduler.start()