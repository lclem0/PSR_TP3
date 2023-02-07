<a name="readme-top"></a>

<h1 align="center">
PSR Trabalho Prático 3 - Robutler
</h1>

![Robutler](./images/robo.jpg?raw=true)

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

![Planta do Apartamento](./images/apartamento.jpg?raw=true "Planta do Apartamento")

O apartamento simulado em **Gazebo** pode ser observado na imagem seguinte:

![Apartamento em Gazebo - psr_apartment](./images/apartamento.gazebo.jpg?raw=true "Apartamento em Gazebo - psr_apartment")

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

![Robô Waffle_pi - Dimensões e peso](./images/waffle_pi.jpg?raw=true "Robô Waffle_pi - Dimensões e peso")

![Robô Waffle_pi - Estrutura](./images/waffle_pi2.jpg?raw=true "Robô Waffle_pi - Estrutura")

No entanto, esta plataforma foi modificada, havendo um aumento da altura da Câmera Raspberry Pi, para que fosse possível ao Robô visualizar certos objetos que possam ser colocados em cima das mesas ou bancadas.

Na seguinte imagem temos uma vista do Robô com a Câmera Raspberry Pi modificada, bem como a sua estrutura:

![Robô Robutler](./images/robutler.jpg?raw=true "Robô Robutler")

## Mapeamento do Cenário

O mapeamento do cenário foi realizado com o auxílio do **ROS Navigation Stack**, que é um conjunto de pacotes ROS que fornecem uma implementação de referência para o algoritmo de mapeamento SLAM e para o algoritmo de navegação baseado em mapas.

Em inglês Simultaneous localization and mapping, também conhecido como SLAM, é o processo de coleta de dados do mundo físico, com a ajuda de inúmeros sensores instalados no robô. Neste caso o sensor utilizado foi o Sensor LiDAR. Os dados são recolhidos e gerados em mapas para navegação posterior. O SLAM torna mais fácil para o robô se localizar, interpretar dados por meio de pontos visuais, construir um mapa e usá-lo para navegar simultaneamente.

O mapa obtido após o mapeamento foi o seguinte:

![Mapeamento do Apartamento](./images/saved_map.jpg?raw=true "Mapeamento do Apartamento")


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

![Percepção de Objetos](./images/object_detection.jpg?raw=true "Percepção de Objetos")

## Missões
Percepção de objetos: O robô deverá ser capaz de identificar e reconhecer objetos no cenário, de modo a ser capaz de interagir com eles de forma adequada.

Movimentação: O robô deverá ser capaz de se movimentar e se deslocar no cenário, para poder realizar suas missões de forma eficiente.


***

<!-- CENARIO DE TESTES -->
<h2 align="center"> Para iniciar o programa </h2>

Para iniciar o **Gazebo** com o mapa do Apartamento, deve executar-se o seguinte comando:
```
roslaunch robutler_bringup gazebo.launch
```
De seguida, para iniciar o **Rviz**, deve executar-se o seguinte comando:
```
roslaunch robutler_bringup bringup.launch
```

Para posicionar o Robô na posição predefinida inicial, deve executar-se o seguinte comando:
```
roslaunch robutler_navigation localization.launch
```

Para spawnar os objetos no cenário, onde o utilizador pode escolher o número de objetos a serem spawnados,  até um máximo de 7, deve executar-se o seguinte comando:
```
rosrun psr_apartment_description spawn_object.py
```

Para ativar a deteção de objetos, deve executar-se o seguinte comando:
```
roslaunch my_object_recognition_pkg yolo_v2_tiny.launch
```

Para enviar o Robô para uma coordenada XYZ RPY, através do terminal, alterando os valores de acordo com os desejados, deve executar-se o seguinte comando:
```
rostopic pub /move_base/goal geometry_messages/poseStamped
```
## Para uma execução mais rápida
Desenvolveu-se um script que permite executar todos os comandos necessários para a execução do programa, de forma a que o utilizador não tenha de executar todos os comandos manualmente. Para isto deve executar-se o seguinte comando:
```
roslaunch robutler_bringup master.launch
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

***
<!-- CONTRIBUTING -->
## Contribuições

Se tiveres ideias para melhorar este projeto, podes criar um fork do repositório e submeter um pedido de pull ou abrir uma questão com a etiqueta "melhoria". A tua ajuda e feedback é muito apreciado. Não te esqueças de mostrar o teu apoio atribuindo uma estrela a este projeto! Obrigado!

1. Dá fork ao projeto 
2. Cria a tua própria branch (`git checkout -b feature/AmazingFeature`)
3. Dá commit ás tuas alterações  (`git commit -m 'Add some AmazingFeature'`)
4. Dá push das tuas alterações para a branch (`git push origin feature/AmazingFeature`)
5. Faz um pedido de pull do projeto original

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

Professor Miguel Oliveira - mriem@ua.pt

***
###### Programação de Sistemas Robóticos 2022/2023 - Universidade de Aveiro