FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /dockapp

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

