# Tarea2_rys

  # Tarea 2 Taller de redes y servicios

## Description

Docker build para servidor de minecraft

## Requisitos Minimos
Se requiere un minimo de 4GB de rams DISPONIBLES a la hora de ejecutar el servidor

### Executing program


* Iniciar con CD a la ruta del folder que contiene Servidor3 y Dockerfile
* Iniciar la build con el comando
```
sudo docker build -t servidor .
```
* Ver imagen creada
```
sudo docker images
```
* Correr la imagen, con los 3 digitos primeros digitos de la ID de la imagen.
```
 sudo docker run --rm -it -p 25565:25565 'ID imagen'
```


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Sebastian Arroyo  
ex. Lucas Ibarra

## Version History

* 1.17.1


## License

This project is licensed under the [MOJANG] License

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
  
  


  
