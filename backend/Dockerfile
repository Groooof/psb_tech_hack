FROM python:3.7
COPY . /code
WORKDIR /code
RUN pip install --no-cache-dir -r requirements/base.txt
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]