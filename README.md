Build container:
```bash
docker build -t fastboot-mysql-tmp mysql/5.7/
```

run test container

```bash
 docker run -e MYSQL_DATABASE=test -e MYSQL_USER=test -e MYSQL_PASSWORD=test -e MYSQL_ROOT_PASSWORD=test fastboot-mysql-tmp mysqld
```

wait till it finish the initialisation process

```bash
docker ps

CONTAINER ID        IMAGE                COMMAND                  CREATED              STATUS              PORTS                                                      NAMES
0d05ae55473f        fastboot-mysql-tmp   "docker-entrypoint..."   About a minute ago   Up 59 seconds       3306/tcp                                                   gifted_nightingale
```

Commit container
```bash
docker stop 0d05ae55473f
docker commit 0d05ae55473f quay.io/whisk/fastboot-mysql:5.7.19
```