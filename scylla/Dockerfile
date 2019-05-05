FROM centos:7

ENV container docker

ADD scylla_bashrc /scylla_bashrc

# Scylla configuration:
ADD etc/sysconfig/scylla-server /etc/sysconfig/scylla-server

# Supervisord configuration:
ADD etc/supervisord.conf /etc/supervisord.conf
ADD etc/supervisord.conf.d/scylla-server.conf /etc/supervisord.conf.d/scylla-server.conf
ADD scylla-service.sh /scylla-service.sh

# Docker image startup scripts:
ADD scyllasetup.py /scyllasetup.py
ADD commandlineparser.py /commandlineparser.py
ADD docker-entrypoint.py /docker-entrypoint.py
# Install Scylla:
RUN curl http://downloads.scylladb.com/rpm/centos/scylla-3.0.repo -o /etc/yum.repos.d/scylla.repo && \
    yum -y install epel-release && \
    yum -y clean expire-cache && \
    yum -y update && \
    yum -y install scylla hostname supervisor && \
    yum clean all && \
    cat /scylla_bashrc >> /etc/bashrc && \
    mkdir -p /etc/supervisor.conf.d && \
    mkdir -p /var/log/scylla && \
    chown -R scylla.scylla /var/lib/scylla

ENV PATH /opt/scylladb/python3/bin:$PATH
ENTRYPOINT ["/docker-entrypoint.py"]

EXPOSE 9042
