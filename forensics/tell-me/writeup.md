# Tell-me

### Dificultad: Fácil

### Descrpcion:

Tengo que contarte una cosa...
Es probable que haya escuchado un poco de más, pero eso más bien parecia una broma.
Más que una conexión segura para lanzar comandos de forma segura.

Recomendamos leer con paciencia :)

### Solución

Se trata de un `pcap` en el que podemos ver que al inicio hay un pequeño ping hacia una ip y luego se realiza una conexión `telnet` (sabiendo que desconocen la palabra cifrado) en la cual podemos ver en texto plano todos los comandos que transfieren y sus resultado.

Si empezamos a leer el contenido de los paquetes, vemos que los comandos los manda letra a por lo que requiere de cierta paciencia a la hora de leer. Se recomienda usar el filtro `telnet.data` para solo ver los paquetes con los datos. 

Leyendo poco a poco nos encontramos con que lista el directorio en el que se encuentra y vemos que exite un fichero llamado `bandera`, un poco sospechoso.

Y luego vemos que ejecuta el comando `cat bandera`. (Entre los paquetes 208-243)

En el paquete siguiente (245) Nos encontramos con el resultado del comando:

`RVRTSUlUX1VHUnt0M2xuM3RfMXNfNGwxdjN9=`

Podemos observar que se trata de un texto codificado en base 64, por lo cual al decodificarlo obtenmos la flag:

`ETSIIT_UGR{t3ln3t_1s_4l1v3}`


