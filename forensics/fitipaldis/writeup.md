# FiTiPaldis
### Dificultad: Medio

### Descrpcion:

A quien no le va a gustar el Rock :)

### Solución

Abrimos el fichero `capture.pcapng` con Wireshark. Podemos ver claramamente que se trata del protocolo ftp y se están descargando y subiendo ficheros.
Para poder ver todos los ficheros con claridad, solo tenemos que exportarlos de la siguiente forma:
`File` > `Export Objects` > `FTP-DATA` 
Saldrá un cuadro de dialogo con todos los ficheros a exportar. Los guardamos todos y procedemos a verlos (más bien escucharlos que son todo audio :)

Una vez visto que el fichero `flag.mp3` tiene poco futuro. Pasamos a centrarnos un poco en el fichero `soldadito-marinero.mp3` dadas las referencias al artista.

Comprobamos los metadatos del fichero.
`exiftool soldadito-marinero.mp3`

[]()

Y podemos observar cierto comentario en los metadatos que nos indica que es aqui (Here)
Ahora si inspeccionamos el sonido, podemos observar cierta forma extraña en el espectograma.

[]()

Si hacemos un poco de zoom, sobre esa zona, podemos leer claramente la flag.
[]()

Flag: `ETSIIT_UGR{t3ln3t_1s_4l1v3}`
