# LittleBird

Descripcion: Como Flappy Bird es demasiado fácil, he decidido complicarlo un poquito. Suerte!! :D

Flag: ETSIIT_CTF{Ch3At1ng_W1th_4nt1Ch3atS_b3_l1k3_:9}

## Writeup

Se nos da un juego tipo Flappy Bird en Unity compilado en Mono. El objetivo es pasarse el juego aunque es muy complicado por la poca distancias entre tuberías.

Una manera rápida de intentar conseguir una alta putuación es intentar cambiar el valor de la puntuación con CheatEngine. En este caso no vamos a poder encontrar la variable que maneja el valor de la puntuación. La lógica del juego se va a encontrar en el fichero `Assembly-CSharp.dll` dentro de la carpeta `Flappy_Data/Managed`. Podemos abrirlo con dnSpy para mirar su contenido.

Tenemos diferentes clases. La que maneja el inicio y fin del juego va a ser la clase `GameManager`.  Dentro de esta clase podemos encontrar funciones interesantes como `IncreaseScore`, `Play`, `Win`, o `GameOver`.

Vamos suponer que la función Win() es la que se llama cuando el jugador gana la partida. Esta se llama desde la función `IncreaseScore()`. Este sería su contenido:

```
public void IncreaseScore()
{
	this.k += 1U;
	this.g.text = this.k.ToString();
	if (this.k >= 10000U)
	{
		this.Win();
	}
}
```

En esta función, se le suma a la variable `k` 1 y se comprueba que `k` sea mayor que 10000. En ese caso, se llama a la función de ganar.
Como no podemos modificar el contenido de la variable dinámicamente vamos a modificar el dll para que en vez de sumar 1 cada vez que se pasa por una tubería, se sume 1000 a la variable. Para ello modificamos el ensamblador IL del índice 4. Cambiamos la instrucción `lcd.i4.1` por `lcd.i4` y le añadimos el valor 1000.

Guardamos el dll y ejecutamos el programa. Con sólo pasar por una tubería se nos mostrará la flag: 

`ETSIIT_CTF{Ch3At1ng_W1th_4nt1Ch3atS_b3_l1k3_:9}`
