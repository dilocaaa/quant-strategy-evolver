from src.evolutionary import example_fitness_function

def test_fitness_function():
    params = [10, 50]
    score = example_fitness_function(params)
    
    assert isinstance(score, float), "La función de fitness debe devolver un float"
    assert score >= 0, "El fitness no puede ser negativo"
