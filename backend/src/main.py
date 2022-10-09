from fastapi import FastAPI
from src import events
from src.assistant.routers import router


def get_app():
    app = FastAPI()
    app.title = 'Цифровой финансовый помощник по кредитным продуктам банка ПСБ---'
    app.description = ''
    app.include_router(router=router)
    app.add_event_handler('startup', events.on_startup)
    app.add_event_handler('shutdown', events.on_shutdown)
    return app


app = get_app()
