FROM alpine
MAINTAINER Gary Ossewaarde <gary.ossewaarde@gmail.com>

# basic flask environment & additional tools for managing
RUN apk add --no-cache nginx bash uwsgi uwsgi-python py3-pip \
	&& pip3 install --upgrade pip

# application folder
ENV APP_DIR /app
RUN mkdir ${APP_DIR} \
	&& chown -R nginx:nginx ${APP_DIR} \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R
WORKDIR ${APP_DIR}


# copy files into container
COPY . /app

# install python prereqs
RUN pip3 install -r /app/requirements.txt

# copy config files into the right spot
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh



ENTRYPOINT [ "/entrypoint.sh" ]