mip = "cmip5"
exp = "historical"
mod = "pr.day.GISS-E2-H.historical.r6i1p1.20000101-20051231.nc"
var = "pr"
frq = "day"
modpath = 'demo_data/CMIP5_demo_timeseries/historical/atmos/day/pr/'
results_dir = 'demo_output/precip_variability/GISS-E2-H/'
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
