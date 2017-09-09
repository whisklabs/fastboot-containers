Build container:
```bash
docker build -t fastboot-postgres-tmp:9.6.5 postgres/9.6/
```

run test container

```bash
 docker run -e POSTGRES_DB=test \
   -e POSTGRES_USER=test \
   -e POSTGRES_PASSWORD=test \
   fastboot-postgres-tmp:9.6.5 postgres
```

wait till it finish the initialisation process

```bash
docker ps

CONTAINER ID        IMAGE                COMMAND                  CREATED              STATUS              PORTS                                                      NAMES
0d05ae55473f        fastboot-mysql-tmp   "docker-entrypoint..."   About a minute ago   Up 59 seconds       3306/tcp                                                   gifted_nightingale
```

Commit container
```bash
docker commit 0d05ae55473f quay.io/whisk/fastboot-postgres:9.6.5
```
