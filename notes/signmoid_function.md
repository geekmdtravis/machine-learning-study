# Sigmoid Function (Logistic Function)

## The Sigmoid Function

The sigmoid function is a mathematical function having a characteristic "S"-shaped curve or sigmoid curve. Often, sigmoid function refers to the special case of the logistic function shown in the first figure and defined by the formula:

$$g(z) = \frac{1}{1+e^{-z}}$$
Where $e$ is the base of the natural logarithm and has the value $2.718281828459045$. Note that the $ln(e) = 1$ (otherwise written as $log_e(e) = 1$) and $log(1) = 0$.

## Deriving Z from the Linear Regression Model

The value of $z$ is given by the equation:

$$f_{\vec{w}b}(\vec{x}) = z = \vec{w} \cdot \vec{x} + b$$

Where $\vec{w}$ is the weight vector, $\vec{x}$ is the input vector and $b$ is the bias.

## Logistic Regression Model

The logistic regression model is a linear model for binary classification. It predicts the probability of an instance belonging to a positive class. The model computes a weighted sum of the input features (plus a bias term), but instead of outputting the result directly like the linear regression model does, it outputs the logistic of this result.

$$f_{\vec{w}x}(\vec{x}) = \frac{1}{1+e^{-(\vec{w}\cdot\vec{x} + b)}}$$

Where $\vec{w}$ is the weight vector, $\vec{x}$ is the input vector and $b$ is the bias.

## Interpreting the Logistic Regression Output

The output of the logistic regression model is a probability. The probability that the instance $\vec{x}$ belongs to the positive class. The logistic function outputs a value between 0 and 1. If the probability is greater than 0.5, then the model predicts that the instance belongs to the positive class. Otherwise, it predicts that it does not. This threshold can be changed, but 0.5 is the most common.

## Cost Function for Logistic Regression

The cost function for logistic regression requires a different loss function.

### Loss Function for Logistic Regression

$$L(f_{\vec{w},b}) = \begin{cases} -log(f_{\vec{w},b}(\vec{x}^{(i)})) &\text{if } y^{(i)} = 1 \\ - log(1 - f_{\vec{w},b}(\vec{x}^{(i)})) &\text{if } y^{(i)} = 0 \end{cases}$$

This produces a convex function, which means that gradient descent is guaranteed to find the global minimum (if the learning rate is not too large and you wait long enough).

### Cost Function for Logistic Regression

$$J(\vec{w},b) = \frac{1}{m} \sum_{i=1}^{m} L(f_{\vec{w},b}(x^{(i)}),y^{(i)})$$

Where $m$ is the number of instances in the dataset. Of note, this cost function is nearly the same as the cost function for linear regression. The only difference is that the loss function is different and we do not divide by 2.

### Simplified Loss Function for Logistic Regression

$$L(f_{\vec{w},b}) = -y^{(i)} log(f_{\vec{w},b}(\vec{x}^{(i)})) - (1 - y^{(i)}) log(1 - f_{\vec{w},b}(\vec{x}^{(i)}))$$

### Simplified Cost Function for Logistic Regression

$$J(\vec{w},b) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} log(f_{\vec{w},b}(x^{(i)})) + (1 - y^{(i)}) log(1 - f_{\vec{w},b}(x^{(i)})) \right]$$
