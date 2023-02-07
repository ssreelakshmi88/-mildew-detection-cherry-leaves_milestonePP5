# Powdery Mildew in Cherry Leaves Detector

## Dataset Content

- The dataset is sourced from Kaggle. We created them a fictitious user story where predictive analytics can be applied in a real project in the workplace.

- The dataset contains +4 thousand images taken from Farmy & Foods crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.


## Business Requirements

- The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.


- To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

     - i. The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.

     - ii. The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?

### Hypothesis

Powdery mildew is a fungal disease affecting wide range of plants. But they can be easily recognized by the white, powdery growth of the fungus on infected portions of plant host. Initially the white or powdery spots appears on top side of the leaves or plant stems. Then gradually it invades the entire leaf.

### Validation

An average image and variability study with an accuracy of 97%  has to be investigated .

A binary classification model is created. The model states:

- Cherry leaves without mildew (healthy)
- Cherry leaves with mildew


## Rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1: Data visualisation

- An average and variability image for each class (healthy or powdery mildew) has been displayed.

- The difference between an average healthy leaf and an average powdery mildew leaf has been shown.

- There will be an image montage for each class of leaf, healthy or powdery mildew.


### Business Requirement 2: Classification of images

- Predict whether the given leaf has powdery mildew or not.

- Build an ML model to predict the images of cherry leaves and classify them using neural network.


## ML Business Case


- From the given dataset of images, we want to construct an supervised, single-label, binary classification ML model to predict if a leaf contains powdery mildew.

- The purpose of this is to provide the Marianne McGuineys team a faster and reliable diagnostic if a given leaf has powdery patches thereby confirming the cherry plants are not healthy.

- Currently the employees spend around 30 minutes in each tree to visually diagnose the powdery mildew disease. The employee then applies a specific compound to kill the fungus. The whole process is time -consuming and it is not scalable.

- The model output is defined as a flag, indicating if the leaf contains any feature that can show that the tree is infected. The staff of the plantation will take a picture of some leaves of the tree and upload them to the App. The prediction is made on the fly.

- The success metric has been set at 97% accuracy on the test set or above.

- The company will benefit by not supplying the market with a product of poor quality through the creation of this mode.

- The training data can be found from Kaggle. This contains 4208 Images. All images are uniformed at (256,256,256,3). To ensure the performance is not affected we will reduce the image shape to something around 50x50.



