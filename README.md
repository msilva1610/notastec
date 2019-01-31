# notastec
Notas técnicas

## Instalação do Redis


### Atualizar o sistema

```
sudo su -
yum update -y
```

### Instalar o EPEL

```
yum install epel-release

˜˜˜

### Instalar o Redis

```
yum install redis -y
``` 

### Iniciar o Redis

```
systemctl start redis.service
```

### Habilitar para iniciar no boot

```
systemctl enable redis
```

## Testando Redis

```
redis-cli ping

```
