# wifi

### Dificultad: Fácil

### Descrpcion:

Si eres hacker entonces sabes sacar la contraseña del wifi :)
Let's Rock You WPA 2 !!!

SSID: `HACK ME`
Flag: ETSIIT_CTF{password}

### Solución

Disponiendo de un ordenador con una interfaz wifi (`wlan0`) y el paquete `aircrack-ng` podemos lograr buscar cual es la clave de la red wifi.

Comenzamos por escanear en busca de la red correspondiente para ello levantamos la interfaz en modo escucha con el siguiente comando.

`sudo airmon-ng start wlan0`

Este comando nos creara la interfaz `wlan0mon` (`wlan0` en `monitor mode`).

[]()

En este punto ubicamos nuestra red que se llama `HACK ME` y tiene la siguiente mac `00:1C:10:9A:10:02`. Como podemos observar en la captura hay un cliente conectado a la red hasta el momento. Por lo cual podemos invitar amablemente a que se desconecte de la red, enviando unos paquetes de deautenticación para que vuelva a conectarse y conseguir el `handshake`. Se puede realizar el ataque de deauth con el siguiente comando

`aireplay-ng --deauth 20 -a 00:1C:10:9A:10:02 -c FF:FF:FF:FF:FF:FF wlan0`

Ahora que disponemos del handshake, podemos realizarle un ataque de fuerza bruta con el siguiente diccionario, para conseguir la constraseña.

`aircrack-ng -w rockyou.txt -b 00:1C:10:9A:10:02 wifi-01.cap`


Una vez obtenida la constraseña: `horoscoop` 
Ya sabemos que la flag es: `ETSIIT_CTF{horscop}`


