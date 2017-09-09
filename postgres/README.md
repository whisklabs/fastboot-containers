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

CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                                                      NAMES
17ef5b286c84        fastboot-postgres-tmp:9.6.5   "docker-entrypoint..."   34 seconds ago      Up 32 seconds       5432/tcp                                                   unruffled_meninsky
```

Commit container
```bash
docker stop 17ef5b286c84
docker commit 17ef5b286c84 quay.io/whisk/fastboot-postgres:9.6.5
```
