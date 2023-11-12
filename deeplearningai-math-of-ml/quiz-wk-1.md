# Quiz - Week 1: Solving Systems of Linear Equations

## Question 1

You are an astronaut on a mission to planet Mars. Using two robotic spacecraft, the Perseverance and Curiosity rovers, your mission is to collect rock samples to bring back to Earth to determine if there is life on the red planet. As a trained astronaut, you know that each rover has a weight limit for samples.

You split the rocks between the two rovers. You first place 2 basalt samples (volcanic rock) and 3 meteorite rocks to Perseverance that weigh 15 grams in total.

You then put 2 basalt samples and 4 meteorites to Curiosity that weigh 16 grams in total. Your goal is to determine how much each sample weighs (b for basalt, m for meteorite). You know that the collected samples are all the same size and shape, so all basalt samples will have the same weight, just as all meteorite samples will have identical weight.

Illustration of a small robot over Mars' surface
To help you calculate the weight of each rock sample, your spacecraft user interface requires you to input the system of equations that represents the weights of the samples on each one of the rovers

$$
\begin{gather}
2b + 3m = 15 \\
2b + 4m = 16
\end{gather}
$$

Represented as a matrix, the system of equations is:

$$
\begin{bmatrix}
2 & 3 & 15 \\
2 & 4 & 16
\end{bmatrix}
$$

The determinant of the matrix is:

$$
\begin{bmatrix}
2 & 3 \\
2 & 4
\end{bmatrix}
$$

This translantes to $2 \times 4 - 2 \times 3 = 2$. Since the determinant is not 0, the system of equations is linearly independent.

The rock samples weights are:

$$
\begin{gather}
2 & 3 & 15 \\
1 & 2 & 8
 \end{gather}
$$

- Divided the second equation by two .

$$
\begin{gather}
1 & 1 & 7 \\
1 & 2 & 8
 \end{gather}
$$

- Subtracted the first equation from the second equation.

$$
\begin{gather}
1 & 1 & 7 \\
0 & 1 & 1
 \end{gather}
$$

- Subtracted the second equation from the first equation.

The result of this is that the first equation is $b + m = 7$ and the second equation is $m = 1$. Therefore, $b = 6$.
