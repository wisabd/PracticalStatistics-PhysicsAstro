from curses.ascii import LF
from xml.sax.handler import property_dom_node
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%

class MH_step:
    def __init__(self,loglike_func,proposal_function):
        self.lf = loglike_func
        self.pf = proposal_function

    def __call__(self,point,loglike):

        updated_p = self.pf(point)
        updated_like = self.lf(updated_p)
        alpha = min(1,np.exp(loglike-updated_like))

        if(alpha<=1.):
            check = np.random.normal(0.,1., size=1)
            if(alpha>check):
                return updated_p, updated_like, True
            else:
                return point, loglike, False
            
#%%
class gaussian_proposal:
    def __init__(self,sigma_step):
        self.n = len(sigma_step)
        self.sigma = sigma_step
    
    def __call__(self,point):
        new_point1 = point[0] + self.sigma[0]*(np.random.normal(0,self.sigma[0], size=1))
        new_point2 = point[1] + self.sigma[1]*(np.random.normal(0,self.sigma[1], size=1))
        new_point = np.array([new_point1,new_point2])

        return new_point

#%%
class LogGaussianLikelihood:
    def __init__(self, y_data,x_data,y_model,sigmas):
        '''
        y_data = parametro da acchiappare
        y_data = modulo di distanza
        x_data = redshift
        MODEL == universe DL
        '''
    
        self.x = x_data
        self.y = y_data
        self.model = y_model
        self.sigma = sigmas
    
    def __call__(self, norm, omega):
        '''
        params = [normalisation factor, omega matter]

        -- calcolo della loglike di un modulo di distanza dato
        -- il modello e l'errore 
        -- quindi alla fine è sul modello che faccio le considerazioni
        FUNZIONE VALE SOLO PER UN PUNTO ALLA VOLTA
        '''        
        #omega matter condition
        if(omega<0. or omega>1.):
           log_like = -1e100
           
        else:            
        #expected values of distance
            dist_mod = self.model(norm,omega,self.x)

            log_like = -0.5* np.sum(((dist_mod-self.y)/self.sigma)**2)
        
        return log_like 

#%% test

import astropy.cosmology as cosmo

def mu_model(norm,omega,z):
    cos = cosmo.FlatLambdaCDM(70,omega)
    distance = 5*np.log10(cos.luminosity_distance(z).value)+norm
    return distance

#%%
data = pd.read_table('SCPUnion2.1_mu_vs_z.txt', comment='#')

z = np.array(data['redshift'])
mu = np.array(data['dist_mod'])
sigma = np.array(data['dist_mod_error'])

print(data.columns)
#print(data['redshift'].head )
#print(np.mean(mu))
print(len(z), len(mu), len(sigma))

#%%