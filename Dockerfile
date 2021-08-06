FROM python:3.8.11

# install requirements.txt
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
&& apt-get install -y --no-install-recommends dialog \
&& apt-get update \
&& apt-get install -y --no-install-recommends openssh-server \
&& echo "$SSH_PASSWD" | chpasswd

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/

# make bash file executable
RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 5000 2222

#COPY sshd_config /etc/ssh/sshd_config
ENTRYPOINT ["init.sh"]