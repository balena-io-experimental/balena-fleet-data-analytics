FROM openjdk:8
RUN export JAVA_HOME=/usr/local/openjdk-8/
RUN apt-get update -y && apt-get install -y build-essential
RUN apt-get install -y curl
RUN mkdir /apache
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.15.0-linux-aarch64.tar.gz
RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-7.15.2-linux-aarch64.tar.gz
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-7.15.0-linux-aarch64.tar.gz
RUN tar -xvzf elasticsearch-7.15.0-linux-aarch64.tar.gz -C /apache
RUN tar -xvzf logstash-7.15.0-linux-aarch64.tar.gz -C /apache
RUN tar -xvzf kibana-7.15.2-linux-aarch64.tar.gz -C /apache
# es has to be run as a non-root user
# RUN useradd -ms /bin/bash newuser && usermod -aG sudo newuser && chown -R newuser /apache
COPY . /apache
RUN mv /apache/elasticsearch.yml /apache/elasticsearch-7.15.0/config/
RUN mv /apache/kibana.yml /apache/kibana-7.15.2-linux-aarch64/config/
# there are issues with using the machine learning expansion inside a docker
RUN echo "vm.max_map_count=262144" >> /etc/sysctl.conf
RUN su newuser -c '/apache/elasticsearch-7.15.0/bin/elasticsearch -q -E xpack.ml.enabled=false' &
RUN su newuser -c '/apache/kibana-7.15.2/bin/kibana' &
ENTRYPOINT ["tail", "-f", "/dev/null"]
                                   