#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#

from PyQt5 import QtGui as Qt, QtCore, QtWidgets

from gnuradio import gr

def check_set_qss():
    app = QtWidgets.qApp
    qssfile = gr.prefs().get_string("qtgui", "qss", "")
    if(len(qssfile) > 0):
        try:
            app.setStyleSheet(open(qssfile).read())
        except:
            print("WARNING: bad QSS file, %s" % (qssfile))
