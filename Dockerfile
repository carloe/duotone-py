FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install /code

ENV PYTHONPATH "${PYTHONPATH}:/code"
ENTRYPOINT ["python", "duotone"]
CMD ["--help"]