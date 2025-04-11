# inkscape-templates

This repository contains the templates and a short user-guide on how to use Inkscape in an efficient way. Note that the tips can be used to create paper figure. The templates use the A0 format in landscape/portrait mode. 

__Always align and distribute__

## User-guide (tips)

This section will go through the basics of working in Inkscape to create a poster. We will discuss how to import a `matplotlib.figure` in a proper way, how to change a `matplotlib.figure` that was saved on a white background to work on a dark background and the font and color parameters to use to ensure the viewers can see properly. We will also discuss how scientific images (_i.e._ tif images) should be imported without loss of image quality (no compression).

When working on a new poster, the user should create a folder containing the Inkscape file and all images/results used in the poster. A folder with the following architecture is recommended, but not mandatory
```
poster_{name of project}/
  poster.svg
  panels/
    logos/
      cervo.png
      ulavel.png
    result1/
      image_original.tif
      image_flatten.tif
      graph.pdf
```

__Always align and distribute__

### Import `matplotlib.figure`

Before importing a `matplolib.figure` we need to save this figure in __PDF__ format. This way, we can easily play with the parameters of the figure in Inkscape. Also, unless necessary, it is recommended to output all created graphs to their respective figure, _i.e._ do not use multiple subplots on the same figure. When saving a `matplotlib` figure it is recommended to use the `savefig` method with arguments as such 
```python
fig.savefig(output.pdf, transparent=True, bbox_inches="tight")
```

Once the `matplotlib.figure` is imported in Inkscape, this is where the fun begins. Here are the steps to follow

1. Ungroup the imported figure using `Ctrl+u` (3 times should be enough). Note. If there is a white background you can simply delete it. 
2. Select all text from figure and select `Text/Remove Manual Kerns`
3. Select text from ticks and labels and press `t`. Change the fontsize to 32 and select font Minion Pro.
4. As you can see all ticklabels and labels are not aligned with the ticks and axes. To align the ticklabels we will use the snapping tool provided by Inkscape on the right. Enable only the following snapping tools : `Snap bounding boxes, Snap midpoints of bounding box edges, Snap cusp nodes, Snap guides`. We can then drag the ticklabels to their corresponding ticks and snap the bounding box midpoints of the ticklabels and the ticks. We can now set a reasonable distance between the ticks and the ticklabels (2 mm distance seems reasonable, X/Y coordinates - 2).
5. If you used labels for the axes, select the ax followed by the label. Go to `Object/Align and Distribute`, select `Relative to : First selected` and align center on horizontal/vertical axis (thanks to Andréanne). Set a reasonable distance between the label and the ticklabels (4 mm distance seems reasonable, X/Y coordinates - 4).
6. Select the axes and in `Object/Fill and Stroke` change the width of the lines to a minimum of 0.5 mm. Change the width of any other lines that are less than 0.5 mm. 
7. If their is a legend in the `matplotlib.figure` select the text and change the fontsize to 28 set the font to Minion Pro. You can then align everything in the legend.
8. Verify that everything is properly aligned!

__Always align and distribute__

### Modify `matplotlib.figure` to dark background

To modify a `matplotlib.figure` to work on a dark background, the user should first follow the steps in the [Import `matplotlib.figure`](#import-matplotlibfigure) section to format the figure. The user should then follow these steps. In most cases, the default colors from `matplotlib` should be fine on a dark background. 

0. (Optional) Change the background color to grey so you can see both white and black lines. To do so, go in `File/Documents Properties/Background Color`.
1. Select text and change the fill color to white.
2. Select ax lines and change the stroke lines to white.

__Always align and distribute__

### Working with scientific images

You should never transform a scientific image (tif) into a .png\.jpp image. Inkscape (and PowerPoint) can work with 8-bit tif images really easily. As most of the image processing (_i.e._ contrast adjustment, scale bars, etc.) will be done in ImageJ (or (Fiji Is Just) ImageJ), here are the steps to follow to export an 8-bit tif image from ImageJ

1. Adjust contrast of the image (or images if multiple channels)
2. Add scale bar. To do so, go into `Analyse/Tools/Scale Bar`. Depending on your image and pixel size set the width of the scale bar (1 µm or 2 µm are commonly used in super-resolution). The width should be consistent throughout the exported images. 
3. Flatten the image using `Ctrl+Shift+f` or `Image/Overlay/Flatten`. The image is now in an RGB format and can be save to tif.
4. Import the saved image to Inkscape.

__Always align and distribute__

### Fonts

The following table references different parameters relative to the fonts used in a poster

Parameters | Value
-----------|-------
Font | Minion Pro
Title fontsize | 96
Authors fontsize | 48 
Affiliations fontsize | 32
Box titles fontsize | 64
Text fontsize | 32
Plot ticklabels and labels fontsize | 32 
Plot legend fontsize | 28

### Colors

The following table references the different colors used in the poster. 

Parameters | Value
-----------|-------
Box title color | 87cdde (135, 205, 222)
Dark background color | 343434 (52, 52, 52)
