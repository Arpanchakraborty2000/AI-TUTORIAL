# 📐 Equation of Line, Plane (3D) & Hyperplane

These concepts are very important in **Linear Algebra** and **Machine
Learning** (especially in algorithms like SVM, Linear Regression,
Logistic Regression).

------------------------------------------------------------------------

# 1️⃣ Equation of a Line (2D)

![2D Line
Graph](https://upload.wikimedia.org/wikipedia/commons/3/3a/Linear_Function_Graph.svg)

## ✅ Slope-Intercept Form

y = mx + b

Where: - m = slope\
- b = y-intercept

Example: y = 2x + 3

------------------------------------------------------------------------

## ✅ General Form

ax + by + c = 0

Example: 2x + 3y - 6 = 0

------------------------------------------------------------------------

## ✅ Vector Form (Used in ML)

w₁x₁ + w₂x₂ + b = 0

Used in: - Linear Regression\
- Logistic Regression\
- Support Vector Machine (SVM)

------------------------------------------------------------------------

# 2️⃣ Equation of a Line in 3D

![3D Line
Example](https://upload.wikimedia.org/wikipedia/commons/6/6b/3D_line.svg)

In 3D, we use **parametric form**:

x = x₀ + at\
y = y₀ + bt\
z = z₀ + ct

Where: - (x₀, y₀, z₀) = point on the line\
- (a, b, c) = direction vector\
- t = parameter

------------------------------------------------------------------------

# 3️⃣ Equation of a Plane (3D)

![3D Plane
Example](https://upload.wikimedia.org/wikipedia/commons/2/2c/Plane_in_3D_space.svg)

## ✅ General Form:

ax + by + cz + d = 0

Where: - (a, b, c) = normal vector to plane\
- d = constant

Example: 2x + 3y + 4z - 5 = 0

------------------------------------------------------------------------

# 4️⃣ Equation of a Hyperplane (n-Dimension)

![Hyperplane SVM
Example](https://upload.wikimedia.org/wikipedia/commons/2/2a/Svm_separating_hyperplanes_%28SVG%29.svg)

A hyperplane is a **generalization of line and plane to higher
dimensions**.

## ✅ General Equation:

w₁x₁ + w₂x₂ + ... + wₙxₙ + b = 0

OR

wᵀx + b = 0

Where: - w = weight vector\
- x = feature vector\
- b = bias

------------------------------------------------------------------------

# 🔥 Understanding by Dimension

  Dimension   Object       Equation
  ----------- ------------ ----------------------
  2D          Line         ax + by + c = 0
  3D          Plane        ax + by + cz + d = 0
  n-D         Hyperplane   w·x + b = 0

------------------------------------------------------------------------

# 🎯 ML Perspective

-   In 2D → Hyperplane becomes a line\
-   In 3D → Hyperplane becomes a plane\
-   In 100D → Same formula applies

Used in: - Support Vector Machine (SVM)\
- Perceptron\
- Logistic Regression

------------------------------------------------------------------------

# 🚀 One-Line Concept

-   Line → separates 2D space\
-   Plane → separates 3D space\
-   Hyperplane → separates n-dimensional space

------------------------------------------------------------------------

⭐ Perfect for GitHub, ML interview preparation, and revision notes.
