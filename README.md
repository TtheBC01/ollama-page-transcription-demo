# Transcribing books with Ollama vision models

Included is a mediocre photograph (taken with an iPhone 13 and converted to jpeg w/ Gimp) of the first page of Methods of Mathematical Physics: Volume 1. The included script and its prompt uses the Ollama inference engine with llama3.2-vision to attempt to accurately transcribe the text. 

The page has multiple subsections and also includes mathematical notation which should make transciption more difficult, especially for such a small multi-modal vision model. Here is an example of what I was able to produce given the prompt: `Extract all of the text from this photograph of a book page exactly as it appears in the image. Output the text in markdown format.`

# CHAPTER I
## The Algebra of Linear Transformations and Quadratic Forms

In the present volume we shall be concerned with many topics in mathematical analysis which are intimately related to the theory of linear transformations and quadratic forms. A brief résumé of pertinent aspects of this field will therefore be given in Chapter 1. The reader is assumed to be familiar with the subject generally.

## Linear Equations and Transformations

The results of the theory of linear equations can be expressed concisely by the notation of vector analysis. A system of n real numbers x_1, x_2, ..., x_n called an n-dimensional vector or a vector in n-dimensional space and denoted by the bold face letter x; the components (i = 1, ..., n) are called the components of the vector x.

If all the components vanish, the vector is said to be zero or the null vector. For n = 2 or n = 3 a vector can be interpreted geometrically as a "position vector" leading from the origin to the point with rectangular coordinates x_1, ..., x_n. For n > 3 geometrical visualization is no longer possible but geometrical terminology remains suitable.

Given two arbitrary real numbers λ and μ, the vector λx + μy = z is defined as the vector whose components are given by z_i = λx_i + μy_i. Thus the sum and difference of two vectors are defined.

## The Number

The number x · y is called the "inner product" of the vectors x and y. Occasionally we shall call the inner product x · y the component of the vector y with respect to x or vice versa.

If the inner product x · y vanishes, we say that the vectors x and y are orthogonal; for n = 2 and n = 3 this terminology has an immediate geometrical interpretation.

This page is a continuation of Chapter I.
