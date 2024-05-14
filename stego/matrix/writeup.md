# Matrix

### Dificultad: Media 

### Descrpcion:
Algunas veces quiero ser como neo y ver los datos binarios como si fueran imagenes, pero la encriptación esta siempre por medio :C

### Solución

La imagen esta encriptada, pero al ser tener la imagen un formato pgm, la imagen se encuentra en un formato donde se indica pixel, tras pixel con lo cual podemos ver como cambia cada pixel al aplicarle el xor. Puesto que la clave no es muy grande, se puede observar el patron de la imagen original pese al cifrado.

Para visualizar la imagen pese a que pierde la cabecera, podemos usar la siguiente herramienta web [Rawpixels](http://rawpixels.net/)

Establecemos el ancho y alto que conocemos gracias a un comentario en el código: `2480x1748`
Y simplemente usamos los ojos para leer la flag :)

Flag: `ETSIIT_CTF{1_c4n_s33_thr0ugh_3ncrypt10n}`

