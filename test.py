from styler import KNNImageStyler
from PIL import Image

# Initialize the class
styler = KNNImageStyler(n_clusters=5, n_neighbors=1, cluster_range=(3, 8))

# Load test images
cat = Image.fromarray(data.chelsea())     # Cat
dog = Image.fromarray(data.coffee())      # Dog-like
land = Image.fromarray(data.rocket())     # Landscape

# Run styling + plotting dynamically
for name, img in [("Cat", cat), ("Dog", dog), ("Landscape", land)]:
    print(f"\n Styling {name} Image ...")
    styler.process_and_plot(img, title_prefix=name)
