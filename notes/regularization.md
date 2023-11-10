# Regularization of the $w$ parameters

In order to avoid over-fitting, we can employ regularization. The regularization term is added to the cost function $J(w, b)$. The regularization term is:

$$\frac{\lambda}{2m} \sum_{j=1}^{n} w_j^2$$

where $\lambda$ is the regularization parameter. The regularization parameter controls the amount of regularization. The regularization parameter is a hyperparameter. The regularization parameter is not learned by the model. The regularization parameter is set by the user. The regularization parameter is usually set to a small value, such as 0.01 or 0.001.

The cost function with regularization is:

$$J(w, b) = \frac{1}{m} \sum_{i=1}^{m} L(f_{w,b}(x^{(i)}),y^{(i)}) + \frac{\lambda}{2m} \sum_{j=1}^{n} w_j^2$$

## The Wrong $\lambda$ Value

If the regularization parameter is too large, the model will under-fit the data. This is because the regularization term will dominate the cost function. The model will be penalized too much for having large values of $w$, $b$, and $w$ and $b$. If the regularization term is too small, the model will over-fit the data. This is because the regularization term will not have much of an effect on the cost function. The model will not be penalized enough for having large values of $w$, $b$, and $w$ and $b$.

In other words, cost $J$ is directly proportional to $\lambda$.

## Implementing Gradient Descent with Regularization

The algorithm for gradient descent with regularization is:

1. Initialize $w$ and $b$ to random values.
2. Calculate the gradient of the cost function with respect to $w$ and $b$.

$$\frac{\partial J(w, b)}{\partial w} = \frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})x^{(i)} + \frac{\lambda}{m}w$$

$$\frac{\partial J(w, b)}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})$$

3. Update $w$ and $b$ by subtracting the gradient from $w$ and $b$.
4. Repeat steps 2 and 3 until the gradient is zero.

Updating looks like:

$$w := w - \alpha\left(\frac{\partial J(w, b)}{\partial w}\right)$$
$$b := b - \alpha\left(\frac{\partial J(w, b)}{\partial b}\right)$$
