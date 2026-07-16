import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUMBER_OF_SIMULATIONS: int = 1000


def stock_monte_carlo(S0: float, mu: float, sigma: float, N: int = 252) -> None:
    """
    :param S0:
    :param mu:
    :param sigma:
    :param N: Number of days, 252 = trading days in a year
    :return: N/A
    """
    result = []

    # Number of simulations
    for _ in range(NUMBER_OF_SIMULATIONS):
        prices = [S0]
        for _ in range(N):
            # Must simulate change day by day (t = 1)
            stock_price = prices[-1] * np.exp((mu - 0.5 * sigma ** 2) + sigma * np.random.normal())
            prices.append(stock_price)

        result.append(prices)

    # Given columns will contain the time series for a given simulation
    simulation_data = pd.DataFrame(result)
    simulation_data = simulation_data.T
    simulation_data['mean'] = simulation_data.mean(axis=1)

    plt.plot(simulation_data['mean'])
    plt.show()
    print('Prediction for future stick price: $%.2f' % simulation_data['mean'].tail(1))


if __name__ == '__main__':
    stock_monte_carlo(50, 0.0002, 0.01)
