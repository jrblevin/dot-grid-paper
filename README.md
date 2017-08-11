# Dot Grid Paper

These are PDF templates for 0.25 inch dot grid paper in US letter format.

## Overview

Since they are in PDF format, the are useful for:

*   Printing your own dot grid paper
*   Templates in apps such as [GoodNotes][] ([iOS][], [macOS][])

Several variations are included:

*   _Orientation:_ portrait and landscape
*   _Margin:_ top margin or full grid
*   _Color:_ white or "antique"

## Package Contents

*   `dot-grid.sty` - A LaTeX package which defines colors, margins, and a dot grid macro using Tikz.
*   `dot-grid.py` - A Python script which generates the TeX files.

## Usage

1.   Run `dot-grid.py` to produce the `.tex` files.
2.   Run `pdflatex` on each `.tex` file as desired.
3.   Use the resulting PDF files.

Or, simply use the included output files in the `pdf` directory.

## Specifications

*   For templates with a top margin, the first two rows of dots are omitted.

*   Antique color is `rgb(255, 255, 244)` or `#fffff4`.

*   Dot color is `rgb(204, 204, 198)` or `#ccccc6`.

*   Dot radius is 0.01 inches.

[GoodNotes]: http://www.goodnotesapp.com
[iOS]: https://itunes.apple.com/us/app/goodnotes-4-notes-pdf/id778658393?mt=8&uo=4&at=11l5Vs
[macOS]: https://itunes.apple.com/us/app/goodnotes/id1026566364?mt=12&uo=4&at=11l5Vs
