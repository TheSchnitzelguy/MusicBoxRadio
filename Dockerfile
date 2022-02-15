
FROM python:3.9-buster
ARG UID=1000
ARG GID=1000
ADD ./musicbox /musicbox
WORKDIR /musicbox
RUN apt update -y
RUN apt install pulseaudio vlc pulseaudio-utils -y
RUN adduser --gecos '' containeruser
RUN usermod -a -G audio containeruser
RUN adduser root pulse-access
RUN adduser containeruser pulse-access
RUN pip3 install -r requirements.txt
USER containeruser
CMD ["python3", "musicBox.py"]

