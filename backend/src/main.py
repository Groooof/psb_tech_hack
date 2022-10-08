from fastapi import FastAPI
from src.assistant.routers import router as router_rest
from src import events


def get_app():
    app = FastAPI()
    app.title = 'Цифровой финансовый помощник по кредитным продуктам банка ПСБ'
    app.description = ''
    app.include_router(router=router_rest)
    app.add_event_handler('startup', events.on_startup)
    app.add_event_handler('shutdown', events.on_shutdown)
    return app


app = get_app()
