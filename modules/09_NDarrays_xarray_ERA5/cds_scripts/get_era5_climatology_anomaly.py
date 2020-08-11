#! /usr/bin/env python

import cdsapi

c = cdsapi.Client()

for v in ['surface_air_temperature','precipitation']:
    c.retrieve(
        'ecv-for-climate-change',
        {
            #'variable':'precipitation',
            'variable':v,
            'product_type':'anomaly',
            'month':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12'
            ],
            'format':'zip',
            'time_aggregation':'1_month',
            'year':[
                '1979','1980','1981',
                '1982','1983','1984',
                '1985','1986','1987',
                '1988','1989','1990',
                '1991','1992','1993',
                '1994','1995','1996',
                '1997','1998','1999',
                '2000','2001','2002',
                '2003','2004','2005',
                '2006','2007','2008',
                '2009','2010','2011',
                '2012','2013','2014',
                '2015','2016','2017',
                '2018','2019','2020'
            ]
        },
        'era5_climatology_%s_anomaly_1month.zip' % v)
