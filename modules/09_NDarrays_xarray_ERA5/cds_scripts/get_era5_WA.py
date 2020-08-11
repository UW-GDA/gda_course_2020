#! /usr/bin/env python

import cdsapi

c = cdsapi.Client()

#Western U.S.  
#'area':[50, -127, 30, -102], # North, West, South, East. Default: global
#WA state
area = [49,-124.75,45.5,-117]

#variables = ['2m_temperature','total_precipitation','snow_depth']
#variables = ['2m_temperature','total_precipitation']
variables = '2m_temperature'
#variables = 'total_precipitation'

#years = '2018'
years = [str(i) for i in range(1979,2020)]

#months = '12'
months = ["{:02d}".format(i) for i in range(1,13)]

days = ["{:02d}".format(i) for i in range(1,32)]

times = '12:00'
#times = ['00:00','06:00','12:00','18:00']
#times = ['00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00']
#times = ["{:02d}:00".format(i) for i in range(0,25)]

#out_fn = 'era5_WA_ppt_1979-2018_1200.grib'
out_fn = 'era5_WA_t_ppt_201812_hourly.grib'

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',
        'format':'grib',
        'variable':variables,
        #'param':'2t/mx2t/mn2t'
        'area':area,
        'year':years,
        'month':months,
        'day':days,
        'time':times, 
    },
    out_fn)
