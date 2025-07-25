import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats, fft, interpolate, integrate, optimize
import sys

class DataAnalyzerSuite:
    def __init__(self, csv_file):
        try:
            self.data = pd.read_csv(csv_file)
            print(f"✅ Data successfully loaded from '{csv_file}'.")
        except FileNotFoundError:
            print(f"❌ Error: File '{csv_file}' not found!")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            sys.exit(1)

    def descriptive_statistics(self, column):
        col_data = self.data[column].dropna()
        desc = stats.describe(col_data)
        print(f"\n📊 Descriptive statistics for '{column}':")
        print(desc)

    def perform_fft(self, column, sampling_rate):
        y = self.data[column].dropna()
        N = len(y)
        T = 1.0 / sampling_rate
        yf = fft.fft(y)
        xf = fft.fftfreq(N, T)[:N//2]
        plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
        plt.title(f"FFT Analysis of '{column}'")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()

    def interpolate_missing_data(self, column, method='cubic'):
        y = self.data[column]
        x = np.arange(len(y))
        mask = np.isfinite(y)
        interpolator = interpolate.interp1d(x[mask], y[mask], kind=method, fill_value="extrapolate")
        y_interp = interpolator(x)
        self.data[column + '_interp'] = y_interp
        plt.plot(x, y, 'o', label='Original Data')
        plt.plot(x, y_interp, '-', label='Interpolated Data')
        plt.title(f"Interpolation ({method}) for '{column}'")
        plt.legend()
        plt.grid()
        plt.show()

    def numerical_integration(self, func, a, b):
        result, error = integrate.quad(func, a, b)
        print(f"\n∫ Numerical integration from {a} to {b} = {result} (±{error:.4e})")

    def optimize_function(self):
        rosen = optimize.rosen
        x0 = np.array([1.3, 0.7])
        res = optimize.minimize(rosen, x0, method='BFGS')
        print("\n🔧 Optimization result (Rosenbrock function):")
        print(f"Minimum at: {res.x}")
        print(f"Function value: {res.fun:.4f}")
        print(f"Success: {res.success}, Message: {res.message}")

def main():
    analyzer = DataAnalyzerSuite('sample_data.csv')
    analyzer.descriptive_statistics('value')
    analyzer.perform_fft('value', sampling_rate=800)
    analyzer.interpolate_missing_data('value', method='cubic')
    analyzer.numerical_integration(lambda x: np.sin(x) + x**2, 0, 10)
    analyzer.optimize_function()

if __name__ == "__main__":
    main()
