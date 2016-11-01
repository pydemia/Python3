import numpy
 
from matplotlib import pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages
 
# Generate the data
data = numpy.random.randn(15, 1024)
 
# The PDF document
pdf_pages = PdfPages('histograms.pdf')
 
# Generate the pages
nb_plots = data.shape[0]
nb_plots_per_page = 5
nb_pages = int(numpy.ceil(nb_plots / float(nb_plots_per_page)))
grid_size = (nb_plots_per_page, 1)
 
for i, samples in enumerate(data):
  # Create a figure instance (ie. a new page) if needed
  if i % nb_plots_per_page == 0:
  	fig = plot.figure(figsize=(8.27, 11.69), dpi=100)
 
  # Plot stuffs !
  plot.subplot2grid(grid_size, (i % nb_plots_per_page, 0))
  plot.hist(samples, 32, normed=1, facecolor='#808080', alpha=0.75)
 
  # Close the page if needed
  if (i + 1) % nb_plots_per_page == 0 or (i + 1) == nb_plots:
    plot.tight_layout()
    pdf_pages.savefig(fig)
 
# Write the PDF document to the disk
pdf_pages.close()
