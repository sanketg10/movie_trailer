FROM python:3-onbuild

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install -r requirements.txt

# Bundle app source
COPY . /usr/src/app

EXPOSE 5000
CMD ["python","./usr/src/app/app.py"]

