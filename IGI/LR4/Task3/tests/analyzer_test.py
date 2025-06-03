import pytest
from Lab4.Task3.series.analyzer import SeriesAnalyzer

@pytest.fixture
def analyzer():
    return SeriesAnalyzer()

def test_statistics(analyzer):
    stats = analyzer.analyze(2.0, 1e-4)
    assert 'mean' in stats
    assert stats['iterations'] > 0
