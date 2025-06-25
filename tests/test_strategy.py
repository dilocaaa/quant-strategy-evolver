import pandas as pd
from src.strategy import simple_moving_average_strategy

def test_strategy_runs():
    # Crear datos simulados
    data = pd.DataFrame({
        'Close': [100, 101, 102, 103, 104, 105, 106, 107]
    })
    result = simple_moving_average_strategy(data, short_window=2, long_window=3)
    assert 'signal' in result.columns
    assert 'positions' in result.columns
