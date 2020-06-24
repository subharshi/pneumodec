# pneumodec

Pneumonia Detection from X-Ray Images

Author : Subharshi Roy

Introduction

Around the world, 16% of every death of children under five worldwide are responsible due to pneumonia. In the United States, near about 1 million people pursue medical aid from hospitals with 50,000 deaths per year [1]. Recently, life-threatening pneumonia complicated coronavirus (COVID-19) disease is proclaiming thousands of lives in 2020. Pneumonia is an inflammatory lung condition which not only involves a single illness but many different illnesses caused by different microorganisms.
The disease starts as an upper respiratory tract infection shifting the infection into the lower respiratory tract. The respiratory bronchioles and alveolar ducts are constantly exposed to microscopic organisms.
The flora of the upper respiratory tract (the nasal passages, the pharynx, paranasal sinuses, and the portion of the larynx above the vocal folds) competes with pathogens in demand for nutrients, while in the lower respiratory tract (the bronchi and bronchioles, the trachea, and the alveoli) the cough reflexes, actions of immunoglobulins and complement proteins, aid in expelling out the mucus and foreign substances [2].
The progression of pneumonia depends on the body’s immune response to the infection, the virulence of the causative organism and the organism load of the pre-stage infection [3].

Dataset Used : Chest X-Ray Images (Pneumonia) by Paul Mooney / Kaggle
Source : https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia


Application of Computer-aided Systems for Medical Diagnosis

The detection of pneumonia disease is commonly performed through the examination of the chest X-Ray radiograph (CXR). The examination involves the diagnosis of the manifestation of the areas of increased opacity, the further diagnosis is confirmed through clinical history, vital signs and various laboratory examinations.
The pneumonia diagnosis on CXR is hectic due to the presence of other scenarios and conditions in the lungs, such as bleeding, fluid overload, loss in volume, post-radiation or post-surgical changes.
There is a known difference or variability amongst radiologists in the interpretation or diagnosis of the chest radiographs.
To improve the efficiency and accuracy of diagnosis, computer-aided systems for pneumonia detection has been widely exploited in the last decade.
Deep learning approaches outperformed or outnumbered conventional machine learning methods in many medical imaging analysis tasks, including detection, classification and segmentation.


Concept of Transfer Learning

Transfer learning is a machine learning methodology where a developed model targeted for a specific task is "reused" as the "starting" point for a model on a second task.
In transfer learning, a base network is trained on a base dataset and task, and then it is used to "repurpose the learned features or transfer them" to a "second target network" to be trained on a target dataset and task.
This process will tend to work if the features are general, meaning suitable to both base and target tasks, instead of specific to the base task.
Tensorflow supports transfer learning with a variety of models with pre-trained weights [4, 5, 6].



VGG16 – Convolutional Neural Network (Classification and Detection)

VGG16 is a convolutional neural network model proposed by K. Simonyan and A. Zisserman from the University of Oxford in the paper “Very Deep Convolutional Networks for Large-Scale Image Recognition”. The model achieves 92.7% top-5 test accuracy in ImageNet, which is a dataset of over 14 million images belonging to 1000 classes. VGG16 was trained for weeks and was using NVIDIA Titan Black GPU’s.

Source : https://neurohive.io/en/popular-networks/vgg16/



References :

1. https://www.scientificanimations.com/pneumonia/

2. https://en.wikipedia.org/wiki/Respiratory_tract#:~:text=The%20upper%20airways%20or%20upper,%2C%20trachea%2C%20bronchi%20and%20bronchioles

3. https://www.visiblebody.com/learn/respiratory/lower-respiratory-system#:~:text=The%20lower%20respiratory%20system%2C%20or,release%20carbon%20dioxide%20in%20exchange

4. https://www.youtube.com/watch?v=mPFq5KMxKVw

5. https://machinelearningmastery.com/transfer-learning-for-deep-learning/
6. https://www.tensorflow.org/api_docs/python/tf/keras/applications )


