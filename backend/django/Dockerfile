FROM python:3.10.1-bullseye
WORKDIR /home/FoodinBackend
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1
RUN apt update && apt install -y netcat
RUN python -m pip install --upgrade pip
COPY ./requirements.pip .
RUN pip install -r requirements.pip --no-binary :all:
COPY . .
ENTRYPOINT ["./entrypoint.sh"]