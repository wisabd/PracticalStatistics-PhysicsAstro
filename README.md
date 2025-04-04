## Description
- These are tutorial projects from the graduate course Practical Statistics for Physics and Astrophysics at University of Bologna taught by Prof. Metcalf

## Problems to be solved
# Tutorial1: Central Limit Theorem


# Tutorial2: Estimate the covariance matrix and find principle components of some data.
- Dataset: A pandas dataframe with 5 columns
- Results: <img width="248" alt="image" src="https://github.com/user-attachments/assets/0e36c9d3-2432-4aca-ba23-f98a57d87817" />
    <img width="270" alt="image" src="https://github.com/user-attachments/assets/64c9e31a-c306-4055-b174-dc14db7c810d" />

  
# Tutorial3: Measure the strength and width of a spectral line using a Bayesian method.
- Dataset:  file tut_03_data.csv. There are three columns: wavelength, flux and sigma. Sigma is the known standard deviation of the flux in each pixel. 
- Results: <img width="326" alt="image" src="https://github.com/user-attachments/assets/1b7d719d-a7d9-4404-ab54-83dccd6c4ed3" />  <img width="295" alt="image" src="https://github.com/user-attachments/assets/48d30bd3-8512-4ffe-80f3-adfb3849aa1e" />


  
# Tutorial4: Determine the spectrographic redshift of a galaxy. To fit a local spectrum with templates using a linear regression and least-squares before trying to estimate the redshift of a redshifted spectrum.
- Dataset:  File localspectrum2.csv contains both the wavelengths and the fluxes of each pixel. 
- Results  <img width="273" alt="image" src="https://github.com/user-attachments/assets/1ab3f5be-0d10-422a-8ece-c2d22dbbcec3" />


# Tutorial5: To estimate the errors in a statistic.
-Dataset: There is noise in the luminosity measurements and we do not know how it is distributed. Read in the luminosity data from the file luminosities.csv
-Results: <img width="287" alt="image" src="https://github.com/user-attachments/assets/d638fb74-11c5-4da5-99dc-27b51f9a8168" />


# Tutorial6: Make and test some linear models for estimated distance modulus μ(z), for Type Ia supernovae (SNe Ia), a key observable in cosmology that relates redshift (z) to the luminosity distance (dL)
-Dataset: Data obtained is from the Supernova Cosmology Project at: http://supernova.lbl.gov/union/descriptions.html#Magvsz     <img width="307" alt="image" src="https://github.com/user-attachments/assets/7d9a1567-5fa9-45f0-b032-c9e40de5cd29" />

-Results:  <img width="612" alt="image" src="https://github.com/user-attachments/assets/4c52c4dd-e6fb-4b74-9e3d-85ba247985be" />


# Tutorial7: To builds models to predict galaxy redshifts from their photometry in 5 bands.
-Dataset:  file reduced_galaxy_data.fits. This file contains a small subset of data from the Slone Digital Sky Survey. The columns in the fits table are: id number, the measured spectroscopic redshift, the fluxes in five bands (ugriz), and the magnitudes in the same five bands.
-Results: <img width="278" alt="image" src="https://github.com/user-attachments/assets/731061ac-d9e2-402b-b4c3-b52f8f8e786e" />


# Tutorial8: Construct a Metropolis-Hastings Markov Chain Monte Carlo (MCMC) sampler and apply it to Type Ia supernova data
-Dataset: supernova data from SCPUnion2.1_mu_vs_z.txt
-Results: <img width="334" alt="image" src="https://github.com/user-attachments/assets/7aca6520-db57-49a5-a571-4ff8d4b0df85" /> <img width="278" alt="image" src="https://github.com/user-attachments/assets/95c38fee-b579-4805-ad3f-3372df65eadf" />



## Technologies used
- matplotlib, numpy, pandas, astropy.io
  
## Screenshots of Plots generated

<img width="212" alt="Screenshot 2025-02-24 073829" src="https://github.com/user-attachments/assets/407a530a-2dfa-4a25-b010-493805dc240c" />
<img width="471" alt="Screenshot 2025-02-24 073433" src="https://github.com/user-attachments/assets/aa6bef9e-f80c-44f3-8d08-4e1b94b35145" />
<img width="223" alt="Screenshot 2025-02-24 073456" src="https://github.com/user-attachments/assets/c888e14d-cc1a-45b5-a0d5-855a074b9677" />
<img width="239" alt="Screenshot 2025-02-24 073730" src="https://github.com/user-attachments/assets/12f165a9-a3ae-48b0-8c13-360d870ae2c6" />
