# 📏 Distance of a Point from a Plane (With Example)

This concept is very important in **Linear Algebra**, **3D Geometry**,
and **Machine Learning** (especially in Support Vector Machine - SVM).

------------------------------------------------------------------------

# 📐 Plane Equation (3D)

A plane in 3D is written as:

ax + by + cz + d = 0

Where: - (a, b, c) = normal vector to the plane\
- d = constant

------------------------------------------------------------------------

# 📍 Geometric Illustration

![Distance of Point from
Plane](https://upload.wikimedia.org/wikipedia/commons/3/3d/Point_to_plane_distance.svg)

The shortest distance from a point to a plane is the **perpendicular
distance**.

------------------------------------------------------------------------

# 📍 Distance Formula

If a point is:

P(x₁, y₁, z₁)

Then the perpendicular distance from the point to the plane is:

Distance = \|ax₁ + by₁ + cz₁ + d\| / √(a² + b² + c²)

------------------------------------------------------------------------

# 🔥 Why This Formula Works?

-   The numerator = projection of point onto normal vector\
-   The denominator = magnitude of normal vector\
-   Absolute value ensures distance is always positive

------------------------------------------------------------------------

# ✅ Example Problem

### Given:

Plane: 2x + 3y + 6z - 5 = 0

Point: P(1, 2, 3)

------------------------------------------------------------------------

## Step 1: Identify values

a = 2\
b = 3\
c = 6\
d = -5

x₁ = 1\
y₁ = 2\
z₁ = 3

------------------------------------------------------------------------

## Step 2: Apply Formula

Distance = \|2(1) + 3(2) + 6(3) - 5\| / √(2² + 3² + 6²)

------------------------------------------------------------------------

## Step 3: Solve

Numerator: 2 + 6 + 18 - 5 = 21

Denominator: √(4 + 9 + 36) = √49 = 7

------------------------------------------------------------------------

# 🎯 Final Answer

Distance = 21 / 7 = 3

------------------------------------------------------------------------

# 🤖 ML Perspective (Very Important)

In SVM, the distance of a data point from the hyperplane is:

\|wᵀx + b\| / \|\|w\|\|

-   Larger distance → Better classification margin\
-   SVM tries to maximize this distance

------------------------------------------------------------------------

# 🚀 One-Line Concept

Distance of point from plane =\
Projection of point onto plane's normal vector

------------------------------------------------------------------------

⭐ Perfect for GitHub notes, ML interviews, and revision.
