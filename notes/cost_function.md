# Cost Function

A cost function is a function that measures the performance of a machine learning model for given data. Cost functions are also called loss functions or error functions. The goal of a machine learning model is to minimize the cost function. The cost function is a function of the model's parameters. The cost function is a measure of how wrong the model is in terms of its ability to estimate the relationship between X and y.

## Linear Regression Formula

The formula for a linear regression model is:

$$h_\theta(x) = \theta_0 + \theta_1x$$ $$or$$ $$f_{x,b}(x) = wx + b$$

where $h_\theta(x)$ is the hypothesis function for the model. The goal of the model is to find the values of $\theta_0$ and $\theta_1$ that minimize the cost function.

Notice that this takes the form of a line:

$$y = mx + b$$

where $m$ is the slope of the line and $b$ is the y-intercept.

## Single Variable Linear Regression

The cost function for a single variable linear regression model is the _mean squared error_ (MSE) cost function. The MSE cost function is defined as:

$$J(\theta_0, \theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)}) - y^{(i)})^2$$

where $h_\theta(x^{(i)}) = \theta_0 + \theta_1x^{(i)}$ is the hypothesis function for the model. The goal of the model is to find the values of $\theta_0$ and $\theta_1$ that minimize the cost function.

Note that the term inside the parenthesis is the difference between the actual value of $y$ and the predicted value of $y$, or the _error_. That value is scared, and the value is summed and divided by the number of samples $m$. Thus the name, _mean squared error_.

The value $2$ is added to the denominator to make the derivative of the cost function easier to calculate. When the derivative is taken, the $2$ that is the result of the squared term cancels out with the $\frac{1}{2}$.
