#! /usr/bin/env python

import sys
import locale
import argparse
locale.setlocale( locale.LC_ALL, '' )
parser = argparse.ArgumentParser()
parser.add_argument('reg',type=float)
parser.add_argument('ot',type=float)
parser.add_argument('--sick',type=float,default=0.0)
parser.add_argument('--holiday',type=float,default=0.0)
parser.add_argument('--pct',type=float,default=1.0)
parser.add_argument('--wage',type=float,default=12.00)
args = parser.parse_args()

toM = locale.currency
def Paystub(rgHr, otHr, sickHr, holHr, w = args.wage):
    w = w*float(args.pct)
    rgPay = round(rgHr * w,2)
    otPay = round(otHr * (w*1.5),2)
    sickPay = round(sickHr * w,2)
    holPay = round(holHr * w,2)
    ttPay = round(rgPay + holPay + otPay + sickPay,2)
    ssc = round(-1*ttPay*0.062,2)
    mc = round(-1*ttPay*0.0145,2)
    fed = round((-1*ttPay*0.15) + 53.80,2)
    st = round((-1*ttPay*0.0795),2)
    np = round(ttPay + ssc + mc + st + fed,2)
    templ = u"{:<40}{:>20}"
    paystub = u'\n'.join([
        templ.format(u"{:>4} Regular Hrs at  {:>6}".format(rgHr, toM(w)),toM(rgPay)),
        templ.format(u"{:>4} Overtime Hrs at {:>6}".format(otHr, toM(w*1.5)),toM(otPay)),
        templ.format(u"{:>4} Sicktime Hrs at {:>6}".format(sickHr, toM(w)),toM(sickPay)),
        templ.format(u"{:>4} Holiday Hrs at {:>6}".format(holHr, toM(w)),toM(holPay)),
        templ.format(u"Gross Wages",toM(ttPay)),
        u'',
        u'Social Security Contribution',
        templ.format(u'Employee pays 6.2%',toM(ssc)),
        u'',
        u"Medicare Contribution",
        templ.format(u"Employee pays 1.45%",toM(mc)),
        u'',
        templ.format(u"State Tax Withholding",toM(st)),
        u"Married, No exemptions: withhold 7.95% of taxable net income",
        u"Source: http://taxes.marylandtaxes.com/Business_Taxes/Business_Tax_Types/Income_Tax/Employer_Withholding/Withholding_Tables/pmtables/2012/0320.pdf",
        u'',
        templ.format("Federal Tax Withholding",toM(fed)),
        u"Married, No exemptions: withhold 15% of taxable income less $53.80",
        u"Source: http://www.irs.gov/pub/irs-pdf/p15t.pdf",
        u'',
        templ.format(u"Net Pay",toM(np)),
    ])
    return paystub


print Paystub(args.reg, args.ot, args.sick, args.holiday)
