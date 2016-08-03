## LaTeX

The .tex files have to be compiled with [xelatex](https://en.wikipedia.org/wiki/XeTeX) in order to use the specified fonts through the [fonspect](https://www.ctan.org/pkg/fontspec?lang=en) package.  

In the preambule, the lines

 \setsansfont[Path = /home/ctroupin/.fonts/]{Cube-Regular2}
 \setromanfont[Path = /home/ctroupin/.fonts/]{DINM2}

have to be adapted according to your installation.

### pdf viewer ###

The colors were not properly reproduced when we open the pdf with Acrobat Reader, thus we added these lines in the tex file:

 \makeatletter%
 \special{pdf: put @thispage <</Group << /S /Transparency /I true /CS /DeviceRGB>> >>}%
 \makeatother%
