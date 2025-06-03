import os
import tempfile
from Lab4.Task3.series.visualization import plot_comparison

def test_plot_generation():
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        plot_comparison([1.5, 2.0, 3.0], 1e-6, tmp.name)
        assert os.path.exists(tmp.name)
        os.unlink(tmp.name)
