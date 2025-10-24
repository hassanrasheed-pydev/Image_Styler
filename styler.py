import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

class KNNImageStyler:
    def __init__(self, n_clusters=5, n_neighbors=1, cluster_range=(2, 12)):
        """
        Initialize the KNN Image Styler.
        
        Args:
            n_clusters (int): Default number of clusters for stylization.
            n_neighbors (int): Number of neighbors for KNN mapping.
            cluster_range (tuple): Range (min, max) for multi-style generation.
        """
        self.n_clusters = n_clusters
        self.n_neighbors = n_neighbors
        self.cluster_range = cluster_range

    def _knn_color_styler(self, image, n_clusters=None, n_neighbors=None):
        """
        Stylize an image using KMeans color reduction + KNN mapping.
        """
        if isinstance(image, Image.Image):
            img = np.array(image)
        else:
            img = image

        h, w, c = img.shape
        pixels = img.reshape(-1, 3)

        n_clusters = n_clusters or self.n_clusters
        n_neighbors = n_neighbors or self.n_neighbors

        # KMeans clustering on colors
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(pixels)
        centers = kmeans.cluster_centers_.astype(np.uint8)

        # KNN color mapping
        knn = NearestNeighbors(n_neighbors=n_neighbors)
        knn.fit(centers)
        _, indices = knn.kneighbors(pixels)
        mapped_pixels = centers[indices.flatten()]

        stylized = mapped_pixels.reshape(h, w, c)
        return Image.fromarray(np.clip(stylized, 0, 255).astype(np.uint8))

    def generate_styles(self, image, cluster_range=None):
        """
        Generate multiple stylized versions across cluster range.
        Returns a dict: {cluster_count: stylized_image}
        """
        cluster_range = cluster_range or self.cluster_range
        styles = {}
        for k in range(cluster_range[0], cluster_range[1] + 1):
            styled = self._knn_color_styler(image, n_clusters=k)
            styles[k] = styled
        return styles

    def plot_styles(self, image, styled_dict, title_prefix=""):
        """
        Display original and stylized versions side-by-side.
        """
        total = len(styled_dict) + 1
        plt.figure(figsize=(3 * total, 4))

        # Original
        plt.subplot(1, total, 1)
        plt.imshow(image)
        plt.title(f"{title_prefix} Original")
        plt.axis("off")

        # Stylized versions
        for i, (k, img) in enumerate(styled_dict.items(), start=2):
            plt.subplot(1, total, i)
            plt.imshow(img)
            plt.title(f"{k} Clusters")
            plt.axis("off")
        plt.show()

    def process_and_plot(self, image, cluster_range=None, title_prefix=""):
        """
        Convenience method: generate + plot in one step.
        """
        styles = self.generate_styles(image, cluster_range)
        self.plot_styles(image, styles, title_prefix)
        return styles
