import pytest
from app import app

def test_header_exists():
    """Test that the header component exists in the layout"""
    layout = app.layout
    # Convert layout to string to check for header
    layout_str = str(layout)
    assert "Pink Morsels Sales Visualizer" in layout_str
    print("✓ Header test passed")

def test_graph_exists():
    """Test that the graph component exists"""
    layout = app.layout
    layout_str = str(layout)
    assert "sales-line-chart" in layout_str
    print("✓ Visualization test passed")

def test_region_filter_exists():
    """Test that the region filter exists"""
    layout = app.layout
    layout_str = str(layout)
    assert "region-filter" in layout_str
    print("✓ Region picker test passed")