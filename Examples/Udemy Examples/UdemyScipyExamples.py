from scipy.stats import norm
import numpy as np

#WE WILL FIND THE PROBALITY FUNCTION OF 0 FROM THE NORMAL GUSIIAN DISTRIBUTION
print(norm.pdf(0))
print(norm.pdf(0, loc= 5, scale=10))

r=np.random.randn(10)
#WE WILL CALACULTE THE PDF OF r

print(norm.pdf(r))

print(norm.logpdf(r))

print(norm.cdf(r))
print(norm.logcdf(r))