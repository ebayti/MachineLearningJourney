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

- This is a rough table to evaluate a model. But there are more in depth analysis for a model to be evaluated such as _specificity, sensitivity, AUC, ROC_.

---
#### 3x3 Confusion Matrix
<img src="https://imgur.com/rXdNlz6.png">
-   Green boxes are the ones where our model did its work.
-   Red ones are bad.

**Take home message**: Size of our confusion matrix is determined by the amount of the stuff we want to predict. Thus, healthy vs patient task had 2x2 matrix, but the favorite movie task had 3x3 (since we restricted the favorite movie choice to those 3).

<a> This is a 4x4 confusion matrix since there are 4 things to predict.
  <img src="https://imgur.com/MRtg2zA.png" />
</a>
---

## Specificity and Sensitivity
### Sensitivity
- The percentage of the correct identification of patients.

--> $$\frac{True Positives}{True Positives + False Negatives}$$
Thus $$142 / (124+29)$$
$$142/171 = 0.83$$
$$Sensitivity= 0.83$$

### Specificity
- The percentage of the correct classification of healthy people.

--> Thus $$\frac{True Negatives}{True Negatives + False Positives}$$

$$110 / (110+22)$$
$$100/132 = 0.8333$$
$$Specificity=0.83$$

###### When comparing different sensitivity and specificity scores
- Decide what is more important for you to predict or classify.
_For example_, if correctly identifying healthy people is more important, you should stich with the high specificity.
_On the other hand,_ if correctly identifying patients is more important, you should stich with the low sensitivity.

###### More general explanation
**Sensitivity** is the percentage of TRUE POSITIVES
**Specificity** is the percentage of TRUE NEGATIVES

---
###### Sensitivity and specificity with 3 or more parameters
  <img src="https://imgur.com/bTRcWnU.png" /> 
 For this type of data; we need to calculate sensitivity and specificity for each parameter.

- For this calculation I added <a href="calculation1.py">calculation1.py</a> script. But the logic works like the below: 
---

**Sensitivity**: since this is the percentage of True Positives we are going to work with actual number of people who loved Troll 2

<img src="https://imgur.com/zwUTjOr.png" />

Therefore; $$Sensitivity=\frac{12}{12+112+83}$$
$$Sensitivity= 0.06$$

True Positives= 12 --> people loved Troll 2 and our algorithm predicted so. 
False Negatives= 195 --> people loved other films but our algorithm predicted Troll 2

---
**Specificity**: since this is the percentage of True Negatives, we will be working with the number of actual people who did not like Troll 2

<img src="https://imgur.com/ejV74vP.png"/>

Therefore; $$Specificity = \frac{23+77+92+17}{23+77+92+17+102+93}$$
$$Specificity=0.52$$

True Negatives= 209 --> people did not pick Troll 2 as their favorite and our model did predict so (23+77+92+17).

False Positives= 195 --> people did not pick Troll 2 as their favorite and our favorite but our algorithm predicted Troll 2

## Bias and Variance
Let's look at the following graph. It shows the relationship between a mice's height and weight.

<a> The curved line shows the relationship between the two parameters.
<img src="https://imgur.com/2QJuac9.png" /> 
</a>

However, we are going to approximate the relationship between the two parameters with a machine learning methods.(after splitting the data into two as training and testing)

##### Linear Regression (least squares)
<img src="https://imgur.com/rSR2cG1.png">

#### Bias
With the training set, we are able to draw this line (Y=mx+b).
Of course, such a line is not covering the real relationship. And it cannot, no matter how much we train the data. This inability is called as **bias**.

We can calculate the bias by calculating the sums of squares. In other words, calculate the distances of data points to the regression line, square them and get the sum.
<img src="https://imgur.com/D8aLP2z.png" alt="sums of squares" />

#### Variance
The difference between the sum of squares of the testing and training data is **variance**
<img src="https://imgur.com/ukvUK85.png" />

To have a _low bias_ and _low variance_ we will resort to **regularization, boosting** and **bagging**.

## Entropy
- Basically it quantifies similarities and differences.
--> Expected suprise for each event.

You can derive entropy with 
$$probability= (p(x))$$ 
and $$suprise=log{\frac{1}{p(x)}} $$
$$ Entropy=  \sum(p(x))log{\frac{1}{p(x)}} $$
after some more derivation;

$$ Entropy= -\sigma(p(x)log{p(x)})
