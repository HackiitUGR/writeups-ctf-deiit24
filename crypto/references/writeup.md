# References

### Dificultad: Fácil

### Descrpcion:

Toda buena referencia empieza con un buen libro, en este caso `La guia del autoestopista galactico`, es una buena novela con un giro pues el numero clave de esta novela es . El libro de base esta bien para comenzar, solo que prefiero que a ese número se le hubiese sumado tres. También es cierto que me encantan los clásicos y en este caso el protagonista es la clave.

Cifrado: `34E0:EV$D5M5QR46098ZBVG8NZBAN86*6RZBRW69*7RY8/:6/1B7+80X5KIBS1`

Recomendable leer bien :)

### Solución
Pasos a seguir en la cadena de "cifrados":
- Decodificamos de la base 45
- Aplicamos una rotación 47, solo que rotando 42 veces
- Desciframos el Vigere con clave 'arthurdent', el nombre del protagonista


Dejo aqui la config de [CyberChef](https://cyberchef.org):

```
Vigenère_Encode('arthurdent')
ROT47(42)
To_Base45('0-9A-Z $%*+\\-./:')
```


