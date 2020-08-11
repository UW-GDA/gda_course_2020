#! /usr/bin/env python

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'ecv-for-climate-change',
    {
        'variable':[
            'precipitation','surface_air_temperature'
        ],
        'product_type':'climatology',
        'month':[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12'
        ],
        'format':'zip'
    },
    'era5_climatology_1981-2010.zip')
