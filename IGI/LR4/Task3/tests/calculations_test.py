from Lab4.Task3.series.calculations import calculate_terms, exact_value

def test_exact_value():
    assert abs(exact_value(2) - 1.098612) < 1e-6

def test_series_convergence():
    terms = calculate_terms(2.0, 1e-6)
    assert len(terms) > 5
    assert terms[-1][2] < 1e-6  # Last term < epsilon
