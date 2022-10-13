FROM python:3.9 as build-python

RUN #apt-get -y update \
RUN apt-get install -y gettext \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

### Final image
FROM python:3.9-slim

RUN groupadd -r app && useradd -r -g app app

RUN #apt-get update \
RUN apt-get install -y \
  gdal-bin \
  libgdal-dev \
  python3-gdal \
  binutils \
  libproj-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/media /app/static \
  && chown -R app:app /app/

COPY --from=build-python /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}
RUN #SECRET_KEY=dummy STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input
ENV PYTHONUNBUFFERED 1
CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "--worker-class", "saleor.asgi.gunicorn_worker.UvicornWorker", "saleor.asgi:application"]