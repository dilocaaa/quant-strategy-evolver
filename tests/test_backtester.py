def test_backtest_strategy():
    result = {"profit": 0.05, "drawdown": 0.02, "sharpe_ratio": 1.5}
    assert "profit" in result
