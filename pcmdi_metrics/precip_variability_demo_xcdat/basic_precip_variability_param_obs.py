mip = "obs"
mod = "pr.day.GPCP-1-3.PCMDI.gn.19961002-20170101.nc"
var = "pr"
frq = "day"
modpath = 'demo_data/obs4MIPs_PCMDI_daily/NASA-JPL/GPCP-1-3/day/pr/gn/latest'
results_dir = 'demo_output/precip_variability/GPCP-1-3/'
prd = [2000,2005]  # analysis period
fac = 86400  # factor to make unit of [mm/day]

# length of segment in power spectra (~10 years)
# shortened to 2 years for demo purposes
nperseg = 2 * 365
# length of overlap between segments in power spectra (~5 years)
# shortened to 1 year for demo purposes
noverlap = 1 * 365

# flag for cmec formatted JSON
cmec = False
