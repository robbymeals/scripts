#! /usr/bin/env python

import sys
import locale
locale.setlocale( locale.LC_ALL, '' )
toM = locale.currency

def valPaystub(rgHr, otHr, sickHr, w = 15.00):
  w = w*float(sys.argv[4])
  rgPay = rgHr * w
  otPay = otHr * (w*1.5)
  sickPay = sickHr * w
  ttPay = rgPay + otPay + sickPay
  ssc = -1*ttPay*0.062
  mc = -1*ttPay*0.0145
  np = ttPay + ssc + mc
  templ = u"{:<40}{:>20}"
  paystub = u'\n'.join([
    u"Wages",
    u"Total Hours: {}".format(rgHr+otHr),
    templ.format(u"Regular Hrs at  ${}".format(w),toM(rgPay)),
    templ.format(u"Overtime Hrs at ${}".format(w*1.5),toM(otPay)),
    templ.format(u"Sicktime Hrs at ${}".format(w),toM(sickPay)),
    templ.format(u"Gross Wages",toM(ttPay)),
    u'',
    u'Social Security Contibution',
    templ.format(u'Employee pays 6.2%',toM(ssc)),
    u'',
    u"Medicare Contibution",
    templ.format(u"Employee pays 1.45%",toM(mc)),
    u'',
    templ.format(u"Net Pay",toM(np)),
  ])
  return paystub

print valPaystub(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
