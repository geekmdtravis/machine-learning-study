# Cost Function

A cost function is a function that measures the performance of a machine learning model for given data. Cost functions are also called loss functions or error functions. The goal of a machine learning model is to minimize the cost function. The cost function is a function of the model's parameters. The cost function is a measure of how wrong the model is in terms of its ability to estimate the relationship between X and y.

## Why Use a Cost Function?

The cost function is used to measure the performance of a machine learning model. The goal of a machine learning model is to minimize the cost function. The cost function is a function of the model's parameters. The cost function is a measure of how wrong the model is in terms of its ability to estimate the relationship between X and y. This is often done through a process of iterating over the model's parameters and minimizing the cost function.

## Review: Linear Regression Formula

The formula for a linear regression model is:

$$f_{x,b}(x) = wx + b$$

Notice that this takes the form of a line:

$$y = mx + b$$

where $m$ is the slope of the line and $b$ is the y-intercept.

## Single Variable Linear Regression

The cost function for a single variable linear regression model is the _mean squared error_ (MSE) cost function. The MSE cost function is defined as:

$$J(w, b) = \frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})^2$$

where $m$ is the number of samples, $x^{(i)}$ is the $i$th sample, $y^{(i)}$ is the $i$th label, and $f_{w,b}(x^{(i)})$ is the predicted value of $y$ for the $i$th sample. Note that the term inside the parenthesis is the difference between the actual value of $y$ and the predicted value of $y$, or the _error_. That value is scared, and the value is summed and divided by the number of samples $m$. Thus the name, _mean squared error_.

The value $2$ is added to the denominator to make the derivative of the cost function easier to calculate. When the derivative is taken, the $2$ that is the result of the squared term cancels out with the $\frac{1}{2}$.

## Plotting

It often helps to visualize the cost function. There are ways to visualize the cost function in 3D, but we will use a contour plot. A contour plot is a plot that shows the value of a function at different points in the input space. The contour plot is a 2D plot, so it is easier to visualize than a 3D plot. The contour plot is a plot of the cost function $J(w, b)$ as a function of $w$ and $b$.

### Two-Dimensional Plot

A two dimensional plot of the cost function is shown below. The x-axis is the value of $w$, the y-axis is the value of $b$, and the z-axis is the value of the cost function $J(w, b)$.

![2D Plot](./images/2d_plot.webp)

### Three-Dimensional Plot

A threed dimensional plot of the cost function is shown below. The x-axis is the value of $w$, the y-axis is the value of $b$, and the z-axis is the value of the cost function $J(w, b)$.

![3D Plot](./images/3d_plot.png)

### Contour Plot

A contour plot of the cost function is shown below. The x-axis is the value of $w$, the y-axis is the value of $b$, and the z-axis is the value of the cost function $J(w, b)$. The contour plot is the one on the right, and for reference the 3D plot is on the left.

![Contour Plot](./images/contour_plot.png)

## Identifying the Minimum

The minimum of the cost function is the point where the cost function is at its lowest value. There may be local minima, but there is always only one global minimum. When using code to find the minimum, it is important to make sure that the minimum is the global minimum and not a local minimum.

### Gradient Descent

Gradient Descent is an algorithmic process of finding the minimum of a function. Gradient Descent is an iterative process. The algorithm starts at a random point, and then it takes a step in the direction of the steepest descent. The algorithm continues to take steps in the direction of the steepest descent until it reaches a point where the gradient is zero. The gradient is zero at the minimum of the function. In terms of the calculus involved, the gradient is the derivative of the function. The derivative of the function is zero at the minimum of the function.

![Gradient Descent](./images/gradient_descent.png)

The algorithm for gradient descent is:

1. Initialize $w$ and $b$ to random values.
2. Calculate the gradient of the cost function with respect to $w$ and $b$.
3. Update $w$ and $b$ by subtracting the gradient from $w$ and $b$.
4. Repeat steps 2 and 3 until the gradient is zero.

Expressed mathematicaly, the algorithm is:

$$w := w - \alpha\frac{\partial J(w, b)}{\partial w}$$

Note that we're using the notation $:=$ to denote assignment. This is because we're updating the value of $w$ and $b$ in each iteration of the algorithm.

The algorithm is repeated until the gradient is zero. The gradient is zero at the minimum of the function. In terms of the calculus involved, the gradient is the derivative of the function. The derivative of the function is zero at the minimum of the function.

The term $\alpha$ is the learning rate. The learning rate is a hyperparameter that controls how fast the algorithm converges. If the learning rate is too small, the algorithm will take a long time to converge. If the learning rate is too large, the algorithm will not converge.

The bias value b is updated in the same way as the weight value w.
The algorithm is:

$$b := b - \alpha\frac{\partial J(w, b)}{\partial b}$$

It is important to note that these should be updated at the same time. Do not update w and b separately. This is because the gradient of the cost function with respect to w and b is a function of both w and b. If you update w and b separately, you will not be updating them in the correct direction.

### Gradient Descent in Linear Regression

We simply need to calculate the gradient of the cost function with respect to w and b. The gradient of the cost function with respect to w is:

$$\frac{\partial J(w, b)}{\partial w} = \frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})x^{(i)}$$

And, with respect to $b$:

$$\frac{\partial J(w, b)}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})$$

[See derivation](https://www.coursera.org/learn/machine-learning/lecture/lgSMj/gradient-descent-for-linear-regression)

Of note, when using the squared error cost function, the cost function with respect to $w$ and $b$ will always have a single global minimum. This is because the cost function is a convex function. A convex function is a function where the line segment between any two points on the function is always above the function. This means that the cost function will always have a single global minimum.

### Gradient Descent in Multiple Variable Linear Regression

$$\frac{\partial J(w, b)}{\partial w} = \frac{1}{m}\sum_{i=1}^{m}(f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})x^{(i)}$$

And, with respect to $b$:

$$\frac{\partial J(w, b)}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}(f_{\vec{w},b}(\vec{x}^{(i)}) - y^{(i)})$$

Note that a vector $\vec{x}$ contains multiple members. For example, $\vec{x} = [x_1, x_2, x_3, ..., x_n]$. The vector $\vec{w}$ is the same. The vector $\vec{w}$ contains the weights for each member of the vector $\vec{x}$. For example, $\vec{w} = [w_1, w_2, w_3, ..., w_n]$.

### Normal Equation as an Alternative to Gradient Descent

Multiple variable linear regression can be solved using the normal equation. The normal equation is:

$$\vec{w} = (X^TX)^{-1}X^T\vec{y}$$

where $X$ is the matrix of samples, $\vec{y}$ is the vector of labels, and $\vec{w}$ is the vector of weights.
