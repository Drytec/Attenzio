FROM python:3.12.3
# Set environment language
ENV LANG C.UTF-8
# update pip ( python install packages )
RUN pip3 install --upgrade pip
# Set working directory
WORKDIR /app
# Copy all from source folder
COPY . .
# install dependencies 
RUN pip3 install -r requirements.txt
# Run service (debug mode)
CMD [ "python3", "manage.py", "runserver" , "0.0.0.0:8000"]
