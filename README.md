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

```

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

## Windows
### Habilitar o Hyper-v

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

### Desabilitar o hyper-v

```
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
```

## Vagrant

```
vagrant plugin install vagrant-vmware-desktop
```
Para funcionar ~e necessário comprar o plug in de licença que custa $75

## CentOS7 Minimal
O Centos minimal image vem com poucos pacotes. Segue os comandos para configuração.

```
yum whatprovides netstat
yum install net-tools
```
