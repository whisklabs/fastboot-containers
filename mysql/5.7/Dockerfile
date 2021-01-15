FROM mysql:5.7.25


# Using separate data folder outside of mysql image declared volume
# https://github.com/moby/moby/issues/3465
# https://medium.com/@stevenlandow/persist-share-dev-mysql-data-in-a-docker-image-with-commit-f9aa9910be0a
RUN mkdir /var/lib/mysql-no-volume

RUN set -exu ;\
 MYSQL_ROOT_PASSWORD=test  docker-entrypoint.sh --datadir /var/lib/mysql-no-volume &\
 MYSQL_PID=$! &&\
 timeout 22 bash -c 'until printf "" 2>>/dev/null >>/dev/tcp/$0/$1; do sleep 1; done' localhost 3306 &&\
 mysql -ptest -e 'create database `test` collate "utf8mb4_unicode_ci"' &&\
 kill $MYSQL_PID &&\
 tail --pid=$MYSQL_PID -f /dev/null # Using tail to wait for PID to end https://unix.stackexchange.com/questions/427115/listen-for-exit-of-process-given-pid

# Using separate data folder outside of mysql image declared volume
# https://github.com/moby/moby/issues/3465
# https://medium.com/@stevenlandow/persist-share-dev-mysql-data-in-a-docker-image-with-commit-f9aa9910be0a
CMD ["--datadir", "/var/lib/mysql-no-volume"]
