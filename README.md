<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">J.A.R.V.I.S. 3000 Finder</h3>

  <p align="center">
    Incorporates the utilization of a deep neural network to categorize objects obtained from 3D models or RGB-D cameras.
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- Introduction -->
## Introduction

The J.A.R.V.I.S. 3000 Finder is an advanced object classification system that uses a deep neural network to identify objects captured from 3D models or RGB-D cameras. This project was developed for an Advanced Industrial Vision Systems class as the second evaluation. The objective is to detect and extract objects from a point cloud and then pass it through a classifier to determine the object's identity and physical characteristics, such as volume and area. 

<!-- ### Built With
* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- GETTING STARTED -->
## Getting Started

For this projet is used [ROS Noetic](http://wiki.ros.org/ROS/Installation) and the object classification CNN is built based on [PyTorch](https://pytorch.org/). To do object detection is used [Open3D](http://www.open3d.org/).

### Prerequisites

To use this code, you need to add the following line in the bashrc or your shell configuration file:

  ```
#J.A.V.I.S Finder mudar para:
export DORA=/home/
export PYTHONPATH="$PYTHONPATH:${HOME}/catkin_ws/src/
  ```
Replace the path of JARVIS to where all the datasets are stored on your computer. You can download the datasets from the project's website. [here](https://rgbd-dataset.cs.washington.edu/).

Update the shell with the new configuration using:
```
source ~/.bashrc
```
If you use zsh, just change to *.zshrc*.
```
source ~/.zshrc
```

Inside the JARVIS folder, there should be a structure similar to: (verificar)
  - models
  - rgbd-dataset
  - rgbd-scenes-v2
    - pc
    - imgs
  - rosbag



### Installation
To install the project, clone the repository inside the *src* folder of your *catkin_ws* and run the following lines:
```
git clone https://github 
cd .. (rever isto)
catkin_make
```

To install all the dependencies of this package, run the following command in your terminal:
```
roscd 
cd ..
p
```
# (verificar)
If you have/want to use a Kinect camera with this project, you can find [here](https://github.com/andrefdre/Dora_the_mug_finder_SAVI/wiki/Instalation#kinect) how to install all the dependencies needed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Train Model
To train the model, run the code:

```
rosrun _train.py -fn <folder_name> -mn <model_name> -n_epochs 50 -batch_size 256 -c 0
```

Where the __*<folder_name>*__ and __*<model_name>*__  should be replaced by the names you want to give. 

***
### Run Object extractor and classifier ( verificar)
To run the detector with previous trained model run the code:
```
roslaunch _finder_bringup d_bringup.launch mn:=<model_name> fn:=<folder_name>
```
Where the __*<folder_name>*__ and __*<model_name>*__ should be replaced by a name for the model previously set while training. 
If you want to visualize extracted images run:
```
roslaunch _finder_bringup d_bringup.launch mn:=<model_name> fn:=<folder_name> visualize:=True
```
It's also possible to add the argument __*audio*__ to initialize audio describing the objects, setting it to true:
```
roslaunch finder_bringup d_bringup.launch mn:=<model_name> fn:=<folder_name> audio:=true
```

***
### Run Kinect
It's also possible to use a kinect camera for processing in real time, by adding the __*kinect*__ argument:
```
roslaunch dora_the_mug_finder_bringup dora_bringup.launch mn:=<model_name> fn:=<folder_name> kinect:=true
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

If you have ideas for improving this project, you can either create a fork of the repository and submit a pull request or open an issue with the label "enhancement". Your support and feedback is greatly appreciated. Don't forget to show your support by giving this project a star! Thank you!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License (verificar)

Distributed under the GPL License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

André Ferreira - andrerferreira@ua.pt

Gonçalo Ribeiro - 

João Cruz - 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Professor Miguel Oliveira - mriem@ua.pt

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/andrefdre/Dora_the_mug_finder_SAVI.svg?style=for-the-badge
[contributors-url]: https://github.com/andrefdre/Dora_the_mug_finder_SAVI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andrefdre/Dora_the_mug_finder_SAVI.svg?style=for-the-badge
[forks-url]: https://github.com/andrefdre/Dora_the_mug_finder_SAVI/network/members
[stars-shield]: https://img.shields.io/github/stars/andrefdre/Dora_the_mug_finder_SAVI.svg?style=for-the-badge
[stars-url]: https://github.com/andrefdre/Dora_the_mug_finder_SAVI/stargazers
[issues-shield]: https://img.shields.io/github/issues/andrefdre/Dora_the_mug_finder_SAVI.svg?style=for-the-badge
[issues-url]: https://github.com/andrefdre/Dora_the_mug_finder_SAVI/issues
[license-shield]: https://img.shields.io/github/license/andrefdre/Dora_the_mug_finder_SAVI.svg?style=for-the-badge
[license-url]: https://github.com/andrefdre/Dora_the_mug_finder_SAVI/blob/master/LICENSE.txt
[product-screenshot]: Docs/logo.svg