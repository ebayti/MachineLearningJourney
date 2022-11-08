# MachineLearning
 In this repo, I will share my machine learning journey. I picked the <a href="https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF">statquest playlist </a> for getting the theoretical backgorund with the fun of learning.

 _Screenshots will be updated and soon_


 ## A Gentle Introduction to Machine Learning
 ### A simple decision tree
 <img src="https://imgur.com/ANj6v3G.png">
    - Decision trees are being used for classification. In general, they are resorted for prediction and classification. Well, the main idea behind the machine learning is making predictions and classifications. This is not a special case for decision trees.

### Simple Linear Regression
 <img src="https://imgur.com/8NblKmM.png">
 - This guy up here is a simple linear regression example. We can basically predict a person's speed by looking at the amount of yam s/he eats. The black dotted line is our model.

 - Dont forget, our aim is to predict, not overfitting!! Eun away from the _Bias-VAriance Tradeoff_

<strong>Terminology:</strong>
- Training data: the original data
- Testing data: new data that we can check our model's performance


## Cross Validation
- A comparison method that allows us to compare different machine learning methods and let us see which one will serve us the best.

* First, estimate the parameters: training part
* Second, evaluate the method:  testing the algorithm 
* Results will reveal what to use:
<img src="https://imgur.com/ks7yCRI.png">

Training the algorithm with the whole data is a big mistake!

    -   Four-Fold Cross Validation (25% - 75%)
    -   Leave One Out Cross Validaion (1% - 99%) _not really popular_
    -   Ten-fold cross validation (%10 - 90%) _popular kid_ 

## Confusion Matrix
<img src="https://imgur.com/kMzrXSg.png">

- **True positives**: Patients that had heart disease and correctly identified by the algorithm  
- **True negatives**: Healthy people that the algotithm classified as healthy 
- **False positives**: Healthy but the alogorithm classified as a patient 
- **False negatives**:Patient but the algorithm classified as healthy

| _Confusion Matrix_ 	| **Actual Patient** 	| **Actual Healhty** 	|
|:---:	|:---:	|:---:	|
| **Predicted Patient** 	| 142 	| 22 	|
| **Predicted Healhty** 	| 29 	| 110 	|

--> This is a rough table to evaluate a model. But there are more in depth analysis for a model to be evaluated such as _specificity, sensitivity, AUC, ROC_.

#### 3x3 Confusion Matrix
<img src="https://imgur.com/rXdNlz6.png">
- Green boxes are the ones where our model did its work.
- Red ones are bad.

**Take home message**: Size of our confusion matrix is determined by the amount of the stuff we want to predict. Thus, healthy vs patient task had 2x2 matrix, but the favorite movie task had 3x3 (since we restricted the favorite movie choice to those 3).

<a> This is a 4x4 confusion matrix since there are 4 things to predict.
  <img src="https://imgur.com/MRtg2zA.png" />
</a>