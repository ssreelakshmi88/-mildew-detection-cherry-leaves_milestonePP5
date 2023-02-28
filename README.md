# Powdery Mildew in Cherry Leaves Detector

Powdery mildew detector is an app that can predict if cherry leaves are healthy or they contain powdery mildew. The app makes prediction, based on an image of a cherry leaf, whether it is a healthy or an infected leaf.

This app is designed based on a supervised, single-label, binary classification ML model. Binary classifier is used to predict the outcome.


![Responsive image](https://user-images.githubusercontent.com/97182442/220570723-07236fbb-b8a5-4b07-ade5-daebadf40371.jpg)


## Dataset Content

- Image dataset is retrieved from Kaggle. In this project, we created a fictitious user story to apply predictive analytics which can be extrapolated to a real world situation.


- The dataset contains more than 4000 images of healthy or diseased cherry leaves taken from Farmy & Foods crop fields. Diseased cherry leaves contain powdery mildew, a fungal disease that affects a wide range of plants. This is a serious concern for the company since it can compromise their product quality. 

The dataset is available at this link: https://www.kaggle.com/datasets/codeinstitute/cherry-leaves


![Kaggle dataset](https://user-images.githubusercontent.com/97182442/221985095-96a6e877-5562-426e-b70b-a4eb8750e07f.jpg)




![kaggle dataset_cherryleaves](https://user-images.githubusercontent.com/97182442/221985173-a70f2577-94f6-49ef-a1a2-0027394656c9.jpg)


## Business Requirements

- Farmy & Foods is facing a challenge with the presence of powdery mildew infection in their cherry plantation. Currently, leaves are manually checked to verify if a particular cherry tree is infected with powdery mildew or not. This time-consuming process takes around 30 minutes for each tree. The infected leaves are then treated with a specific compound to eliminate infection. The time required for this treatment is around 1 minute. With thousands of cherry trees located in multiple farms spread across the country, this detection process is highly inefficient.of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

- To increase efficiency, the IT team suggested establishing a ML system that is capable of differentiating healthy or powdery mildew infected leaf based on images. This initiative, if successful, can be extended to rapidly detect and treat other infected crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

The client is interested in developing an app that can


   i. differentiate healthy and powdery mildew cherry leaves based on images.

   ii. predict, based on an image, if the leaf can be classified as a healthy or infected.


## Hypothesis and how to validate?

### Hypothesis

- A leaf affected by powdery mildew exhibits several features that can differentiate them from healthy ones. Typical characteristics of infected leaf include display of particular marks/signs and morphological changes.  For example, leaves being light in color and roughly-circular. Additional indistinguishable feature is the presence of powder-looking patches on young and susceptible leaves. 

- An Image Montage can define a typical powdery mildew leaf based on the presence of fine white marks. On the other hand, studies based on Average Image, Variability Image, and Difference between Averages didn't reveal any clear pattern to differentiate leaves.


- The ML model will be able to distinguish between a healthy and an infected cherry leaf with at least 97% accuracy.


## Rationale to map the business requirements to the Data Visualizations and ML tasks


### Business Requirement 1: Data visualisation

- As a  client I want to display the "mean" and "standard deviation" of healthy cherry leaf images and cherry leaves that contain powdery mildew, so that I can visually differentiate both the leaves

- As a client I want to display the difference between an average cherry leaf that is healthy and a cherry leaf infected with powdery mildew, enabling to visually distinguish between them.

- As a client I want to display an image montage for cherry leaves that are healthy and cherry leaves that contain powdery mildew, so that I can visually differentiate cherry leaves.


### Business Requirement 2: Classification of images

- As a client I want to predict if a given cherry leaf is a healthy or contains powdery mildew.

- As a client I want to build a ML model and generate reports.


## ML Business Case


- From the given dataset of images, we want to construct a supervised, single-label, binary classification ML model to predict if a leaf contains powdery mildew.

- The purpose of this model is to provide a faster and reliable diagnostic app to screen if a given leaf has powdery patches thereby confirming the cherry plants are not healthy.

- Currently the disease is identified manually and it takes around 30 times for each tree. The process is very time-consuming and it is not scalable.

- The model output is defined as a flag, indicating if the leaf contains any feature that can show that the tree is infected. The staff of the plantation will take a picture of some leaves of the tree and upload them to the App. The prediction is made on the fly.

- The success metric has been set at 97% accuracy on the test set or above.

- The company will benefit by improving the quality of their product.

- The training data can be found from Kaggle. This contains 4208 Images. All images are uniformed at (256,256,256,3). To ensure the performance is not affected we will reduce the image shape to something around 50x50.

## Dashboard Design

### Wireframes

Wireframes have been used for designing the layout of dashboard. Wireframes can be found here:



![Project Summary Page](https://user-images.githubusercontent.com/97182442/220577226-d1926098-cc03-4b53-8137-afe66649996c.png)


![Leaves Visualizer Page](https://user-images.githubusercontent.com/97182442/220577297-0ae2b70c-c9b1-4da9-a58d-1a9f6a00ecc9.png)

![Mildew Detector Page](https://user-images.githubusercontent.com/97182442/220577487-1299e316-61bd-491e-9a31-f4c9c2c42a99.png)


![Project Hypothesis Page](https://user-images.githubusercontent.com/97182442/220577257-d2046f17-85cc-4dfc-bb21-dc62a7d3b816.png)


![ML Performance Page](https://user-images.githubusercontent.com/97182442/220577352-fc59edb9-ccbe-401a-821c-2ec80db7702e.png)

A dashboard is set to present the models and data to the client.

My dashboard consists of a side navigation bar linking to 5 different pages. The details of the pages are as follows:

#### Page 1: Quick Project Summary

- General Information
   - Powdery mildew is a parasitic fungal disease caused by Podosphaera clandestina in cherry trees. Infected plants display white powdery spots on the leaves and stems. The lower leaves are the most affected.
   
   - As the infection progresses, the spots get larger and denser and it may spread to other parts of plant.
   
   - The disease occurs mostly in high humid and moderate temperatures showing devastating effects on the life of the host plant reducing plant harvest.
   
- Project Dataset

    - The available dataset contains 4208 thousand images taken from different leaves, half infected and half healthy.

- Link to additional information

- Business Requirements

    - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.

    - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.



![Project Summary](https://user-images.githubusercontent.com/97182442/220570941-99e3e5ff-3002-419a-8613-01b27e3df6f1.jpg)


#### Page 2: Leaves Visualizer

- Business requirement 1

     - Checkbox 1 - Difference between average and variability image
	 - Checkbox 2 - Difference between average healthy and infected leaves
	 - Checkbox 3 - Image Montage

![Leaves Visualizer](https://user-images.githubusercontent.com/97182442/220571007-5008e34a-25b9-466c-a8a7-3adc6f040b24.jpg)


![Average and variability image](https://user-images.githubusercontent.com/97182442/220571183-580af90f-673d-401c-b6fb-6d65d148c255.jpg)



![Average healthy and infected leaves](https://user-images.githubusercontent.com/97182442/220571261-53507a4d-ca0e-4f4e-8f33-3ad54e21cac0.jpg)




![Image montage_healthy](https://user-images.githubusercontent.com/97182442/220571339-84495978-4955-47c6-8ba3-ae32b2c9a052.jpg)



![Image montage_powdery mildew](https://user-images.githubusercontent.com/97182442/220571372-7946fdb3-cf97-4b46-8d59-6460e729ec99.jpg)


#### Page 3: Powdery Mildew Detector

- Business requirement 2

     - Link to download a set of healthy and not healthy leaves images for live prediction.
     - User Interface with a file uploader widget. The user should upload leaves images. It will display the image and a prediction statement, indicating if the leaf is healthy or not.
     
     - Table with image name and prediction results.

     - Download button to download table.


![Mildew detector page](https://user-images.githubusercontent.com/97182442/220571082-e97588fa-361e-4fe4-9873-c03b159486fb.jpg)

![Prediction](https://user-images.githubusercontent.com/97182442/220571458-8b48479d-b78c-445c-812e-f9b92c7e032d.jpg)

#### Page 4: Project Hypothesis and Validation

- This page displays the project hypothesis and the validation.


![Hypothesis and Validation](https://user-images.githubusercontent.com/97182442/220571541-4cc0652b-98ee-47bf-ae9d-bd8081d76f7c.jpg)


#### Page 5: ML Performance Metrics


**Label Frequencies for Train, Validation and Test Sets**

•	Train - healthy: 1472 images
•	Train - powdery_mildew: 1472 images
•	Validation - healthy: 210 images
•	Validation - powdery_mildew: 210 images
•	Test - healthy: 422 images
•	Test - powdery_mildew: 422 images


![Label frequencies](https://user-images.githubusercontent.com/97182442/220571590-063effb7-458a-475f-b204-d64f84495897.jpg)


**Model History - Accuracy and Losses**

![Model History](https://user-images.githubusercontent.com/97182442/220571610-fa8ca470-25fb-4075-81bf-8d9f7021a6e5.jpg)


**Model Evaluation result**


![Generalized performance](https://user-images.githubusercontent.com/97182442/220571774-c9e52a95-09f5-42ae-8e08-a18c02500db6.jpg)

## Technologies Used

### Languages

Python

### Frameworks and other technologies

1. **Git**: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

2. **GitHub:** GitHub is used to store the projects code after being pushed from Git.

3. **Balsamiq**: Balsamiq is used to create wireframes.

4. **Heroku**: It is a container-based cloud platform used for deployment.

### Data Analysis and Machine Learning Libraries 

Following are the list of libraries used in the project

1. **Numpy**: It is an open-source, python library used for working with arrays. NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines.

2. **Pandas**: It is an open-source, python package used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.

3. **Matplotlib**: It is a cross-platform, data visualization and graphical plotting library for python.

4. **Seaborn**: It is Python data visualization library based on Matplotlib. It will be used to visualize random distributions.

5. **Plotly**: It is an interactive, open-soource, and browser-based gra6.	Tensorflow: It is an open-sourec machine learning platform focused on deep neural networks.phing library. Used to create visualisations within Jupyter notebooks to present the data.

6. **Tensorflow**: It is an open-source machine learning platform focused on deep neural networks.

7. **Shutil**: Used form file copying and removal.

8. **Streamlit**: It is used to create web apps for data science and machine learning.

9. **Joblib**: It is a set of tools  to provide lightweighting pipelining in Python.

10. **PIL**: Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.


### Bugs

- Initially when I creates an app on Heroku, the stack by default does not support the Python version that I was using, so I had to change the stack of my project from 22 to 20.

- The slug size was also too large. So I added the extra large files in .slugignore file.


### Deployment

1. The App live link is: https://cherry-leaf-mildew-detector.herokuapp.com/

2. The project was deployed to Heroku using the following steps.

  -  At the Deploy tab, select GitHub as the deployment method.

  - Select your repository name and click Search. Once it is found, click Connect.

  - Select the branch you want to deploy, then click Deploy Branch.
 - The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

## Credits

- [Code Institute Malaria Walk Through Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/) : The code and design was taken from  Code-Institute-Org/WalkthroughProject01. I only made minor changes. This project helped me to understand the concept of Machine Learning and Data Analytics.

- [GyanShashwat1611/WalkthroughProject01](https://github.com/GyanShashwat1611/WalkthroughProject01) github repository was used for code reference and assistance for in the jupyter notebook set up, code and execution; as well as for the app pages design, set up and code

- HaimanotA/Instant-Mildew-Detector github repository was used for app pages code reference and readme guidance.

- [alerebal/Powdery Mildew] (https://github.com/Code-Institute-Submissions/milestone-project-mildew-detection-in-cherry-leaves.git) in Cherry Leaves Detector: Readme guidance

### Content

- Streamlit lessons by Code Institute

- Streamlit documentation

- Wikipedia for understanding powdery mildew fungal infection.

### Acknowledgements

My mentor **Precious Ijege** for support and guidance.

Code Institute slack community



