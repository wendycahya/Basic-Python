from scipy.interpolate import interp1d

m = interp1d([0, 10], [-1, 1])
m(0)
print("Hasil scale: ", m(0))
