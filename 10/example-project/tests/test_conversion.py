from spaceship import convert_liter_to_gallon

def test_convert_liter_to_gallon():
    assert abs(convert_liter_to_gallon(1) - 0.264172) < 1e-6
    assert abs(convert_liter_to_gallon(10) - 2.64172) < 1e-6
    assert abs(convert_liter_to_gallon(0) - 0.0) < 1e-6
    assert abs(convert_liter_to_gallon(3.78541) - 1.0) < 1e-5  # Approximately 1 gallon
    