FROM ubuntu:latest 

RUN apt-get update \
    && apt-get --assume-yes upgrade 

RUN apt-get install --assume-yes python \
    && apt-get install --assume-yes pip \
    && pip install boto3 

COPY ./securityGroup.py /opt/securityGroup.py 

CMD python /opt/securityGroup.py 