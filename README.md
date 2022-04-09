# About The Project

During the pandemic COVID-19, the World Health Organization (WHO) advised the use of masks as part of a comprehensive package of prevention and control 
measures to limit the spread of this virus.This project is focused on Real time face mask detection algorithm using machine learning with Python.

## Libraries used
* Tensorflow
* Keras
* OpenCV
* numpy

## Setup
To run this project, install the libraries locally using pip:
```
pip install tensorflow
pip install numpy
pip install matplotlib
pip install opencv
```

## Summary of code

<h4>The project can be divided into three parts: </h4>

<h5>1. Reshaping and Normalizing images in dataset.</h5>

<p>Here we are customizing our dataset to make it perfect for our model. The images are resized and augmented using imagedatagenerator and stored separately for train and validation.</p>
<h5>2. Creation and training of model using tensorflow.</h5>

<p>Now after creating sets for training and validation next step is to build the model.The model is built using convolutional neural networks(CNN), Maxpooling layers and Dense layers along with activation functions Relu and sigmoid.</p>

<p>After model is created it needs to be compiled.For compilation the loss function used is categorical crossentropy,optimizer used is Adam.</p>

<p>Now its time to train our model with the images in train set. The model is trained with train set, validation set and checkpoints to save after completing 100 steps in each epoch.Once the training is complete the model is saved in .h5 format.</p>

<h5>3. Using trained model in opencv to detect face-mask.</h5>

<p>Using opencv we can take input image through our webcam. Using cascade classifiers in opencv we can fetch the face area and use our trained model to predict whether the person is wearing face-mask or not.</p>
  
## Testing the model in Real-time

<p align="center">
  <img src="pictures/2022-04-01 (9).png" alt="..." >
</p>
<p>
  <img src="pictures/2022-04-01 (10).png" alt="...">
</p>


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement" or "feature".
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
