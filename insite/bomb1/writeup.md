# wifi

### Dificultad: Fácil

### Descrpcion:

No te preocupes que no explota, eso fue lo que le dije al profesor antes de traer tal dispositivo de destrucción mas iva. Claro esta que le deje el código para que supiera desconectarlo, pero se me olvido la contraseña. Descifralo, miralo y luego atrevete a desactivarla.

Lets Rock You the bomb code.

### Solución

Para descifrar el código se puede usar:

`fcrackzip -u -D -p /media/data/Downloads/rockyou.txt bomb.zip`

Cuyo resultado seria que la contraseña es: `princesa`. Con eso ya podemos ver el código y desactivarla.

Simplemente corta el cable correcto. Que si ves el código se trata del cable que sale del pin `11`. Como se puede ver en el siguiente código.

```c
if (digitalRead(11) == LOW) {
	// Deactivated
	mensajeVictoria();
}
```


