## Description
- These are tutorial projects from the graduate course Practical Statistics for Physics and Astrophysics at University of Bologna taught by Prof. Metcalf

## Background for projects 
- Task 1: To measure the strength and width of a spectral line task using Bayesian parameter estimation.  A spectral line is a dark or bright line in an otherwise uniform and continuous spectrum, resulting from the emission or absorption of light at specific wavelengths by atoms, molecules, or ions. Spectral lines are key features in spectroscopy and are used to study the physical properties of astronomical objects, such as their composition, temperature, density, and velocity. Whereas bayesian parameter estimation is a statistical method that uses Bayes' theorem to update the probability of a hypothesis (e.g., the strength and width of a spectral line) as more evidence (e.g., observational data) becomes available. Bayesian appraoch involves:
Defining a model: A mathematical function that describes the spectral line (e.g., a Gaussian profile for the line and a polynomial for the continuum).

Incorporating prior knowledge: Using prior information about the parameters (e.g., the expected wavelength of the line, the range of possible strengths, etc.).

Fitting the data: Using the flux and sigma values to find the most likely parameters of the model, given the data and the priors.

Estimating uncertainties: Providing a range of possible values for the parameters, along with their probabilities

- Task 2: Linear Regression
- Task 3: Photometric redshift

## Datasets used
- For linear regression task, the dataset in this tutorial is stored in a FITS (Flexible Image Transport System) file named k_nmf_derived.newdefault.fits. The dataset contains template spectra, which are rest-frame galaxy spectra used for comparison. These templates represent different types of galaxies or stellar populations.


- For the photometric redshift tutorial the dataset is as following:

| Column Name              | Description |
|--------------------------|-------------|
| `id`                     | Unique identifier for the galaxy |
| `spectroscopic redshift` | Measured redshift (used as the target variable) |
| `fluxes (ugriz)`         | Observed flux values in **five photometric bands** (u, g, r, i, z) |
| `magnitudes (ugriz)`     | Corresponding magnitudes in the **same five bands** |

- For Bayesian parameter estimation to measure the strength and width of a spectral line task, the data is in  tut_03_data.csv. There are three columns: wavelength, flux and sigma. Sigma is the known standard deviation of the flux in each pixel. Spectrum has been plotted using matplotlib.pyplot.errorbar() 


These are the 3 datasets used

<p align="left">
  <img width="242" alt="Screenshot 2025-02-24 125343" src="https://github.com/user-attachments/assets/477f9de0-35ef-4e60-9c25-755e5f143d97" />
  <img width="244" alt="image" src="https://github.com/user-attachments/assets/ab765e24-574a-4747-823f-56dceb4849ab" />
  <img width="227" alt="image" src="https://github.com/user-attachments/assets/cc8d8ea8-1a05-4d90-8bf6-b9d2c112af69" />
</p>

## Technologies used
- matplotlib, numpy, pandas, astropy.io
  
## Screenshots of Plots generated

<img width="212" alt="Screenshot 2025-02-24 073829" src="https://github.com/user-attachments/assets/407a530a-2dfa-4a25-b010-493805dc240c" />
<img width="471" alt="Screenshot 2025-02-24 073433" src="https://github.com/user-attachments/assets/aa6bef9e-f80c-44f3-8d08-4e1b94b35145" />
<img width="223" alt="Screenshot 2025-02-24 073456" src="https://github.com/user-attachments/assets/c888e14d-cc1a-45b5-a0d5-855a074b9677" />
<img width="239" alt="Screenshot 2025-02-24 073730" src="https://github.com/user-attachments/assets/12f165a9-a3ae-48b0-8c13-360d870ae2c6" />
