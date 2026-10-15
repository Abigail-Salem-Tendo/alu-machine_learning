#!/usr/bin/env python3
"""Normal distribution class representation and estimation."""


class Normal:
    """Represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize a Normal distribution instance."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean_val = sum(data) / len(data)
            # Using sample variance (ddof=1 -> len(data) - 1)
            variance = sum((x - mean_val) ** 2 for x in data) / (len(data) - 1)
            stddev_val = variance ** 0.5

            self.mean = float(mean_val)
            self.stddev = float(stddev_val)

    def z_score(self, x):
        """Calculates the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score."""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value."""
        pi = 3.1415926535
        e = 2.7182818284
        coefficient = 1 / (self.stddev * (2 * pi) ** 0.5)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coefficient * (e ** exponent)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value."""
        val = (x - self.mean) / (self.stddev * (2 ** 0.5))
        
        sign = 1 if val >= 0 else -1
        val_abs = val if val >= 0 else -val

        p = 0.3275911
        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429

        t = 1.0 / (1.0 + p * val_abs)
        e = 2.7182818284
        poly = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t
        erf_val = sign * (1.0 - poly * (e ** (-val_abs * val_abs)))

        return 0.5 * (1.0 + erf_val)
    