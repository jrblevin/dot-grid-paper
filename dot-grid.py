#!/usr/bin/python

orientations = [ 'portrait', 'landscape' ]
colors = [ 'white', 'antique' ]
styles = [ 'full', 'margin' ]

for orientation in orientations:
    for color in colors:
        for style in styles:
            fn = 'dot-grid-%s-%s-%s.tex' % (orientation, color, style)
            print "Generating %s..." % fn
            f = open(fn, 'w+')
            f.write("\\documentclass[%s]{article}\n" % orientation)
            f.write("\\usepackage[dot%s]{dot-grid}\n" % style)
            f.write("\\pagecolor{%s}\n" % color)
            f.write("\\begin{document}\n")
            f.write("\\dotgrid\n")
            f.write("\\end{document}\n")
            f.close()
