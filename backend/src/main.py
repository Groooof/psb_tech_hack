from fastapi import FastAPI
from src import events
from src.assistant.routers import router
from fastapi.middleware.cors import CORSMiddleware


def get_app() -> FastAPI:
    """
    Инициализация и настройка объекта приложения fastapi.
    :return: объект FastAPI
    """
    app = FastAPI()
    app.title = 'Цифровой финансовый помощник по кредитным продуктам банка ПСБ---'
    app.description = ''
    app.include_router(router=router)
    app.add_event_handler('startup', events.on_startup)
    app.add_event_handler('shutdown', events.on_shutdown)
    app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    return app


app = get_app()
