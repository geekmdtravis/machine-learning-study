# Systems of Linear Equations

## System of Sentences

It is important to understand the language of mathematics, translated into the language of linear algebra. There are three types of sentences in linear algebra:

1. **Complete:** A sentence that is true or false. For example, $x + 2y = 5$ is a complete sentence.
2. **Redundants**: A sentence that is always true. For example, $2x + 4y = 10$ is a redundant sentence because it is always true if $x + 2y = 5$ is true.
3. **Contradictory**: A sentence that is always false. For example, $2x + 4y = 11$ is a contradictory sentence because it is always false if $x + 2y = 5$ is true.

Translating the above into a more simple-to-understand variant using cats and dogs, we can say:

1. **Complete:**
   1. The dog is black
   2. The cat is orange
2. **Redundant**:
   1. The dog is black.
   2. The dog is black.
3. **Contradictory**:
   1. The dog is black.
   2. The dog is orange.

### Singular vs. Non-Singular Systems

A non-singular system is complete. A singular system will be either redundant or contradictory.

|     System 1      |     System 2     |     System 3     |     System 4      |
| :---------------: | :--------------: | :--------------: | :---------------: |
| The dog is black  | The dog is black | The dog is black | The dog is black  |
| The cat is orange | The dog is black | The dog is black | The dog is white  |
|  The bird is red  | The bird is red  | The dog is black |  The bird is red  |
|   **Complete**    |  **Redundant**   |  **Redundant**   | **Contradictory** |
| **Non-singular**  | **Non-singular** | **Non-singular** |   **Singular**    |

## Example System of Linear Equations + Challenge

You go two days in a row and collection this information:

- Day 1: You bought an apple and a banana, and they cost $10
- Day 2: You bought an apple and two bananas, and they cost $12

Question: How much does each fruit cost?

$$
\begin{gather}
x + y = 10 \\
x + 2y = 12
\end{gather}
$$

Translated into matrix form:

$$
\begin{bmatrix}
1 & 1 & 10 \\
1 & 2 & 12
\end{bmatrix}
$$

Operations to solve this matrix:

1. Subtract row 1 from row 2
2. Division is not necessary, but it is a good practice to do so and we would get $y = 2$ if we did divide by 1.

$$
\begin{bmatrix}
1 & 1 & 10 \\
0 & 1 & 2
\end{bmatrix}
$$

From this, we can see that $y = 2$. And, with that we can deduce that $x = 8$.

You'll also notice that you can subtract the new row 2 from row 1 to get $x = 8$.

A variant.
You go two days in a row and collection this information:

- Day 1: You bought an apple and a banana, and they cost $10
- Day 2: You bought an apple and two bananas, and they cost $20

Question: How much does each fruit cost?

$$
\begin{bmatrix}
1 & 1 & 10 \\
2 & 2 & 20
\end{bmatrix}
$$

Operations to solve:

1. Subtract row 1 from row 2
2. Check for division (not necessary)

$$
\begin{bmatrix}
1 & 1 & 10 \\
1 & 1 & 10
\end{bmatrix}
$$

From this, we can see that $x + y = 10$ and $x + y = 10$. This is a redundant system. We can't solve this system because there are infinite solutions.

Put more simply, the system has the same information twice, and therefore it is classified as redundant.

$ 2 * (x + y) = 2*10 $ provides no more information than $x + y = 10$.

Another variant.
You go two days in a row and collection this information:

- Day 1: You bought an apple and a banana, and they cost $10
- Day 2: You bought an apple and two bananas, and they cost $24

Question: How much does each fruit cost?

$$
\begin{bmatrix}
1 & 1 & 10 \\
2 & 2 & 24
\end{bmatrix}
$$

Operations to solve:

1. Subtract row 1 from row 2

$$
\begin{bmatrix}
1 & 1 & 10 \\
1 & 1 & 14
\end{bmatrix}
$$

From this, we can see that $x + y = 10$ and $x + y = 14$. This is a contradictory system. We can't solve this system because there are no solutions.

## Linear Dependence Between Equations

A system of linear equations is linearly dependent if one of the equations can be derived from the other equations. For example:

$$
\begin{gather}
x + y = 10 \\
2x + 2y = 20
\end{gather}
$$

Or, in matrix form:

$$
\begin{bmatrix}
1 & 1 & 10 \\
2 & 2 & 20
\end{bmatrix}
$$

It's clear that the second equation can be derived from the first equation. Therefore, this system is linearly dependent.

## The determinant of a matrix: A means of determining linear dependence

The determinant of a matrix is a means of determining linear dependence. If the determinant is 0, then the system is linearly dependent. If the determinant is not 0, then the system is linearly independent.

$$
\begin{bmatrix}
1 & 1  \\
2 & 2
\end{bmatrix}
$$

The determinant of this matrix is 0. Therefore, this system is linearly dependent.

$$
\begin{bmatrix}
1 & 1  \\
2 & 3
\end{bmatrix}
$$

The determinant of this matrix is 1. Therefore, this system is linearly independent.

### Calculating the determinant of a matrix

$$
\begin{bmatrix}
a & b  \\
c & d
\end{bmatrix}
$$

The determinant of this matrix is $ad - bc$.
