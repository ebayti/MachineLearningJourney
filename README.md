# Machine Learning
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

- For this calculation I added <a href="pythonscripts/specificity_sensitivity_calculation.py">a python script</a>. But the logic works like the below: 
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

$$Entropy=  \sum(p(x))log{\frac{1}{p(x)}}$$

after some derivation it becomes;

$$ Entropy= -\sum(p(x)log{p(x)})$$

Entropy is highest when same number of different events, and it decreases when there is different events with different amounts.
  <img src="https://imgur.com/3tu4S51.png" />

# Linear Regression

<a>> It is good to know the trend of our data, or even have a summarized version of it.
  <img src="https://imgur.com/3nYJ3tx.png" />
</a>

_But, how to find the best/optimal line_

#### Generic line equation
$Y=mx+b$

m-> slope of the line

b-> intercept (x=0)

** For finding the optimized line, we seek to minimize sums of squared residuals**
<img src="https://imgur.com/CDeJPVN.png" />
They are the differences between the real data (the observed value of the given x) and the model (calculated value of the given x) .

$$ Sum of squared residuals= \sum ((mx_1+b)-y_1)^2$$
- Finding the best m and b is called **least squares**.
 - <small> Least squares will ignore the useless parameters by setting their weight to zero. Thus, useless ones will not effect the performance of the model. But they are not required :D </small>

###### How do we look for the best?
- Plot the sum of squared residuals and take their derivatives to get slope. When the $\frac{df}{dx}=0$, it is the best!

  <img src="https://imgur.com/tFd55ix.png" />

#### The main ideas behind Linear Regression
1- Use least squares (sums of squared residuals)
2- Calculate the $R^2$
3- Calculate the p-value of the $R^2$

<a> This the fitted line with the equation of $y=0.1+0.78x$

<img src="https://imgur.com/x5Y7AZu.png" />

</a>

### $R^2$
-> Does our _least squares_ fits the data better than the mean?

$$R^2= \frac{Var(mean)-Var(fit)}{Var(mean)}$$

$Variance= \frac{SS}{n}$
* SS = Sum of Squares
* n = number of data/things/stuff
* Var(fit) can never be greater than the Var(mean) since Var(mean) is the raw variation in the data

Thus, _variance_ is the **average sum of squares**!

$R^2$ tells us that whether we have less variation around the line than the mean. In other words, the line (mouse size/weight relationship) explains the x% of the variation!!

--> i.e Heavier mices are bigger and vice versa.

$R^2= \frac{The variation in the data explained by x}{The variaton in the data without taking x into account}$

<a> Basically the proportion of variance in mouse size explained by mouse weigth to the variance of the mouse size (raw variance).
  <img src="https://imgur.com/xw4eECe.png" />
</a>

### $F$ p-value for $R^2$ 

$F= \frac{The variation in the data explained by x}{The variaton in the data not explained by x}$
 

<a > The denominator of F is basically the average sum of residuals of the fit!!!!
  <img src="https://imgur.com/VTYXi6Y.png" />
</a>

$$F= \frac{(SS(mean-SS(fit))/(P_{fit}-P_{mean}))}{(SS(fit)/n-P_{fit})))}$$

**$P_{fit}$**= number of parameters for fit. Which is $Y=mx+b$ Thus it is 2; intercept and the slope. Basically, this equation shows the number of extra parameters we have in the fit.

**$P_{mean}$**= number of parameters of the mean. Which is $Y=b$. Thus 1; only the intercept.

Good fit --> Large F value.

-> We calculate the p-value by comparing the F value of our fit and F value of randomly generated data and their fit. If the chance of getting an equal or higher value is huge, then our p-value is not good enough.

_P-value is number of more extreme values divided by all the values_ 

##### Linear Regression Summary
**1)** Linear Regression quantifies the relationship in the data;
  - how well our parameters explain the variance in the data: $R^2$
    - $R^2$ should be large!
**2)** Linear Regression determines the reliability of our quantified relationship.
  - $F$ and $p-value$.
    - $F$ should be large, $p-value$ should be small!


# Multiple Regression
<a> Simple vs Multiple Regression
  <img src="https://imgur.com/5NLXU2W.png" />
</a>
- Calculating the $R^2$ is the same

- Calculating $p-value$ is a bit different. Because $P_{fit}$ is 3 or more when we are dealing with multiple regression.

#### If you want to compare simple vs multiple regression
- $F$ eqaution will differ. We will omit the $SS(mean)$ and replace it with $SS(simple)$.

$$ F = \frac{SS(simple)-SS(multiple)/ P_{multiple}-P_{simple}}{SS(multiple)/(n-P_{multiple})} $$

If the $F$ is big and the $p-value$ is small; conducting a multiple regression is a good idea!