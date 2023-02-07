<a name="readme-top"></a>

<h1 align="center">
PSR Trabalho Prático 3 - Robutler
</h1>

<!-- SUMARIO -->
<h2 align="center"> Sumário </h2>

Neste trabalho pretende-se desenvolver um sistema robótico que funcione como um mordomo, o **Robutler**. Temos como objetivos colocar o Robô a realizar variadas acções e missões habitualmente realizadas por trabalhadores humanos.

O robô tem desenvolvidas várias funcionalidades que suportem a operacionalização destas missões, tais como a perceção de objetos e a movimentação no cenário.

<!-- CENARIO DE TESTES -->
<h2 align="center"> Cenário de Testes </h2>

O Cenário de Testes que será utilizado para testar o robô é um **Apartamento T3 que será simulado em Gazebo**, chamado ***psr_apartment***. 

Este apartamento é composto por:

- **1 Cozinha;**
- **3 Quartos (1 Duplo e 2 Simples);**
- **1 Sala de Estar;**
- **1 Vestíbulo;**
- **2 Instalações Sanitárias;**
- **1 Terraço.** 

O cenário será composto por vários objetos populando o apartamento, tais como: cadeiras, mesas, sofás, televisões, frigoríficos, armários, etc.

A **planta** do apartamento pode ser observada na imagem seguinte:

![Planta do Apartamento](https://github.com/github/lclem0/PSR_TP3/blob/images/apartamento.jpg?raw=true "Planta do Apartamento")

O apartamento simulado em **Gazebo** pode ser observado na imagem seguinte:

![Apartamento em Gazebo - psr_apartment](/repository/images/apartamento_gazebo.jpg?raw=true "Apartamento em Gazebo - psr_apartment")

<!-- OBJETIVOS -->
<h2 align="center"> Objetivos </h2>

Nas seguintes secções serão apresentados os objetivos do projeto, bem como as funcionalidades que o Robô possui. 

## Configuração do Robô
O Robô utilizado foi baseado num ***Turtlebot3 Waffle_pi***. 

O Robô possui as seguintes características, observáveis na listagem seguinte:

- **Dimensões: 281 mm x 306 mm x 141 mm;**
- **Peso: 1.8 kg ;**
- **1 Sensor LiDAR;**
- **1 Câmara Raspberry Pi;**
- **1 Estrutura Escalável;**
- **2 Rodas;**

Nas duas imagens seguintes observa-se o Robô e as características mencionadas anteriormente:

![Robô Waffle_pi - Dimensões e peso](/repository/images/waffle_pi.jpg?raw=true "Robô Waffle_pi - Dimensões e peso")

![Robô Waffle_pi - Estrutura](/repository/images/waffle_pi2.jpg?raw=true "Robô Waffle_pi - Estrutura")

No entanto, esta plataforma foi modificada, havendo um aumento da altura da Câmera Raspberry Pi, para que fosse possível ao Robô visualizar certos objetos que possam ser colocados em cima das mesas ou bancadas.

Na seguinte imagem temos uma vista do Robô com a Câmera Raspberry Pi modificada, bem como a sua estrutura:

![Robô Robutler](/repository/images/robutler.jpg?raw=true "Robô Robutler")

## Mapeamento do Cenário

O mapeamento do cenário foi realizado com o auxílio do **ROS Navigation Stack**, que é um conjunto de pacotes ROS que fornecem uma implementação de referência para o algoritmo de mapeamento SLAM e para o algoritmo de navegação baseado em mapas.

Em inglês Simultaneous localization and mapping, também conhecido como SLAM, é o processo de coleta de dados do mundo físico, com a ajuda de inúmeros sensores instalados no robô. Neste caso o sensor utilizado foi o Sensor LiDAR. Os dados são recolhidos e gerados em mapas para navegação posterior. O SLAM torna mais fácil para o robô se localizar, interpretar dados por meio de pontos visuais, construir um mapa e usá-lo para navegar simultaneamente.

O mapa obtido após o mapeamento foi o seguinte:

![Mapeamento do Apartamento](/repository/images/saved_map.jpg?raw=true "Mapeamento do Apartamento")


## Movimentação do Robô pelo Apartamento
O Robô desenvolvido é capaz de se movimentar pelo cenário, de forma a realizar as suas missões. 

A sua movimentação pode ser feita de várias formas, tais como:
- Por condução manual com teleop:
    - Por teclado (WASD);
    - Por trackbars (GUI).
- Por condução autónoma com o auxílio do ROS Navigation Stack:
    - Por condução autónoma para um alvo expresso em coordenadas X,Y;
    - Por terminal (comandos ROS);
    - Por condução autónoma para um alvo expresso com informação semântica;
    - Por marcadores de navegação. 


## Perceção
Para a perceção do Robô dos variados objetos que serão spawnados, utilizou-se o **Yolo v2 Tiny**, que é um modelo de reconhecimento de objectos que utiliza redes neurais convolucionais para detetar objectos em imagens. 

Este modelo foi treinado para reconhecer 80 classes de objectos diferentes, como por exemplo pessoas, carros, bicicletas, etc.

O modelo foi treinado com o auxílio do **Darknet**, que é uma biblioteca de rede neural convolucional gratuita e de código aberto, escrita em C e CUDA.

Na imagem seginte pode ser observado os resultados obtidos com o modelo Yolo v2 Tiny ao longo dos objectos existentes no Apartamento:

![Percepção de Objetos](/repository/images/object_detection.jpg?raw=true "Percepção de Objetos")

## Missões
Percepção de objetos: O robô deverá ser capaz de identificar e reconhecer objetos no cenário, de modo a ser capaz de interagir com eles de forma adequada.

Movimentação: O robô deverá ser capaz de se movimentar e se deslocar no cenário, para poder realizar suas missões de forma eficiente.

## Missões
Realização de tarefas domésticas: O robô mordomo deverá ser capaz de realizar tarefas domésticas, como limpar a casa, cozinhar e organizar o ambiente.

Atendimento a convidados: O robô deverá ser capaz de atender a convidados, oferecendo bebidas e comidas, e ajudando em suas necessidades.

Auxílio no cuidado de pessoas idosas ou deficientes: O robô mordomo deverá ser capaz de auxiliar pessoas idosas ou deficientes, ajudando-as em suas atividades diárias e garantindo sua segurança.



***
## Getting Started

For this projet is used [ROS Noetic](http://wiki.ros.org/ROS/Installation)

### Installation
To install the project, clone the repository inside the *src* folder of your *catkin_ws* and run the following lines:
```
git clone https://github.com/lclem0/PSR_TP3.git
cd .. 
catkin_make
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

***
### Launch the program
To the map open, with gazebo do:
```
roslaunch robutler_bringup gazebo.launch
```
To add the .....
```
roslaunch _finder_bringup d_bringup.launch mn:=<model_name> fn:=<folder_name> visualize:=
```
***
<!-- CONTRIBUTING -->
## Contributing

If you have ideas for improving this project, you can either create a fork of the repository and submit a pull request or open an issue with the label "enhancement". Your support and feedback is greatly appreciated. Don't forget to show your support by giving this project a star! Thank you!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- CONTACTOS -->
## Contactos

André Ferreira - andrerferreira@ua.pt

João Clemente - jclemente@ua.pt

Mateus Araújo - mateus.araujo@ua.pt

Rafael Mendes - mendes.rafael@ua.pt


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- AGRADECIMENTOS -->
## Agradecimentos

* Professor Miguel Oliveira - mriem@ua.pt
