from scipy import stats
from numpy import log, exp, sqrt

# S =
# E = Strike Price
# T = Expiry Time, in years
# rf =
# sigma =
# t = defined time before T


def call_option_price(S: float, E: float, T: float, rf: float, sigma: float) -> float:
    d1 = (log(S / E) + (rf + sigma * sigma / 2) * T) / sigma * sqrt(T)
    d2 = d1 - sigma * sqrt(T)
    print('d1: ', d1)
    print('d2: ', d2)

    return S * stats.norm.cdf(d1) - E * exp(-rf * T) * stats.norm.cdf(d2)


def put_option_price(S: float, E: float, T: float, rf: float, sigma: float) -> float:
    d1 = (log(S / E) + (rf + sigma * sigma / 2) * T) / sigma * sqrt(T)
    d2 = d1 - sigma * sqrt(T)
    print('d1: ', d1)
    print('d2: ', d2)

    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(-d2)


if __name__ == '__main__':
    S0 = 100        # Stock price a t = 0
    E = 100         # Strike Price
    T = 1           # 1 year
    rf = 0.05       # Risk-free rate
    sigma = 0.2     # Volatility of the underlying stock

    print('Call option price according to the Black-Scholes Model: ', call_option_price(S0, E, T, rf, sigma))
    print('Put option price according to the Black-Scholes Model: ', put_option_price(S0, E, T, rf, sigma))
