from pymc import Normal, Uniform, MvNormal, Exponential
from numpy.linalg import inv, det
from numpy import log, pi, dot
import numpy as np
from scipy.special import gammaln
 
def _model(data, robust=False):
    # priors might be adapted here to be less flat
    mu = Normal('mu', 0, 0.000001, size=2)
    sigma = Uniform('sigma', 0, 1000, size=2)
    rho = Uniform('r', -1, 1)
 
    # we have a further parameter (prior) for the robust case
    if robust == True:
        nu = Exponential('nu',1/29., 1)
        # we model nu as an Exponential plus one
        @pymc.deterministic
        def nuplus(nu=nu):
            return nu + 1
 
    @pymc.deterministic
    def precision(sigma=sigma,rho=rho):
        ss1 = float(sigma[0] * sigma[0])
        ss2 = float(sigma[1] * sigma[1])
        rss = float(rho * sigma[0] * sigma[1])
        return inv(np.mat([[ss1, rss], [rss, ss2]]))
 
    if robust == True:
        # log-likelihood of multivariate t-distribution
        @pymc.stochastic(observed=True)
        def mult_t(value=data.T, mu=mu, tau=precision, nu=nuplus):
            k = float(tau.shape[0])
            res = 0
            for r in value:
                delta = r - mu
                enum1 = gammaln((nu+k)/2.) + 0.5 * log(det(tau))
                denom = (k/2.)*log(nu*pi) + gammaln(nu/2.)
                enum2 = (-(nu+k)/2.) * log (1 + (1/nu)*delta.dot(tau).dot(delta.T))
                result = enum1 + enum2 - denom
                res += result[0]
            return res[0,0]
 
    else:
        mult_n = MvNormal('mult_n', mu=mu, tau=precision, value=data.T, observed=True)
 
    return locals()
 
def analyze(data, robust=False, plot=True):
    model = pymc.MCMC(_model(data,robust))
    model.sample(50000,25000)
 
    print
    if plot:
        pymc.Matplot.plot(model)
 
    return model
    
    
    
#%%
import numpy as np
x = np.array([525., 300., 450., 300., 400., 500., 550., 125., 300., 400., 500., 550.])
y = np.array([250., 225., 275., 350., 325., 375., 450., 400., 500., 550., 600., 525.])
data = np.array([x, y])
model = analyze(data)
