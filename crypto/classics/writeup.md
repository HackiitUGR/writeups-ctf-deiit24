### Descrpcion:

War Classics 紫

December comes.
Days get shorter.
There’s a nip in the air
over Pearl Harbor.

— George Hocking

Flag: ETSIIT_CTF{WORD-WORD...}

### Solución

1. Primero leemos con atención la descripción del reto, con ello podemos ver que el reto tiene relación con la segunda guerra mundial y en especifico con Japón.

2. Con ayuda de San Google Translate, pordemos traducir ese caracter en japones 紫 = purple (morao en andaluz :) Tras una busqueda rápida podemos averiguar que el cifrado usado por los japonese en la segunda guerra mundial es el Purple Cipher.

3. Si vemos a continuación el contenido del fichero `msg.txt`, observamos el siguiente código morse:

`.--- ..- .--- --- -- .- -- -.-- .-- . .... --.. --.. . -... .. ...- .-.. . -.-.`

Se puede decodificar usando cualquier herramienta en linea y obtener el siguiente texto:

`JUJOMAMYWEHZZEBIVLEC`

Dado que a primera vista parece unos golpes de teclado con mucha rabia y antes hemos visto referencias al cifrado japones, podemos suponer que esta cifrado con ello.

4. Buscamos otra vez alguna herramienta que nos permita descifrar el texto y encontramos la siguiete libreria (Python)[https://github.com/gremmie/purple], herramienta desarrollada recientemente y se puede instalar usando 'pip'.

```bash
pip install purple
```

5. Desciframos usando la herramienta

```bash
purple -d -t "JUJOMAMYWEHZZEBIVLEC"
```
Resultado: `JAPAN ESEPU RPLEC IPHER`

6. Formateamos la flag tal y como nos indican en la descripción:
`ETSIIT_CTF{JAPANESE-PURPLE-CIPHER}`

Demasiada creatividad se ha utilizado para la elección de la flag :)

