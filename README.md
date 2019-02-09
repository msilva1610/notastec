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

## Instalando o Virtualbox no Ubuntu com dual boot
### Instalando os pré requisitos

```
sudo apt-get update
sudo apt-get upgrade
```
### Configurando o Apt repositório

```
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
```

### Oracle VirtualBox PPA

```
sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian xenial contrib"
``` 

### Instalar o virtualbox

```
sudo apt-get update
sudo apt-get install virtualbox-5.2
virtualbox
```
### Tive o seguinte erro

```
~$ sudo /sbin/vboxconfig
vboxdrv.sh: Building VirtualBox kernel modules
vboxdrv.sh: Starting VirtualBox services
vboxdrv.sh: Building VirtualBox kernel modules
vboxdrv.sh: failed: modprobe vboxdrv failed. Please use 'dmesg' to find out why
There were problems setting up VirtualBox.  To re-start the set-up process, run   /sbin/vboxconfig as root
```
### Como foi resolvido

Tive que entrar na bios de desabilitar o security boot UEFI.

link: https://ubuntuforums.org/showthread.php?t=2350741
