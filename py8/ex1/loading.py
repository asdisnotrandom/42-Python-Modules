from importlib import metadata
from importlib import util
import sys


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    if util.find_spec("pandas") is not None:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - "
              f"Data manipulation ready")
    else:
        print("[KO] pandas - pandas could not be imported."
              " Use 'pip install pandas' or 'poetry add pandas'")
        sys.exit()
    if util.find_spec("numpy") is not None:
        import numpy
        print(f"[OK] numpy ({numpy.__version__}) - "
              f"Numerical computation ready")
    else:
        print("[KO] numpy - numpy could not be imported."
              " Use 'pip install numpy' or 'poetry add numpy'")
        sys.exit()
    if util.find_spec("matplotlib") is not None:
        import matplotlib.pyplot as plt
        print(f"[OK] matplotlib ({metadata.version('matplotlib')}) - "
              f"Visualization ready")
    else:
        print("[KO] matplotlib - matplotlib could not be imported."
              " Use 'pip install matplotlib' or 'poetry add matplotlib'")
        sys.exit()
    print()
    print("Analyzing Matrix data...")
    data_list: numpy.ndarray = numpy.random.randn(2, 500)
    print(f"Processing {data_list.size} data points...")
    proc_data: pandas.DataFrame = pandas.DataFrame(data_list,
                                                   index=["Signal1", "Signal2"]
                                                   )
    cumsum_data: pandas.DataFrame = proc_data.cumsum(axis=1)
    print("Generating visualization...")
    pic, axis = plt.subplots(2, 1)
    axis[0].plot(
        cumsum_data.loc["Signal1"],
        color="blue"
                )
    axis[1].plot(
            cumsum_data.loc["Signal2"],
            color="red"
                )
    print("Analysis complete!")
    pic.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")
