FROM python:latest

# Install app
ADD . /usr/src/ff_bot
WORKDIR /usr/src/ff_bot
RUN python3 setup.py install

# Launch app
CMD ["python3", "scpfl/ff_bot.py"]