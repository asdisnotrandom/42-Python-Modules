from importlib import metadata
from importlib import util


if __name__ == "__main__":
    if util.find_spec("pandas") is not None:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - "
              f"Data manipulation ready")
    else:
        print("[KO] pandas - pandas could not be imported."
              " Use 'pip install pandas'")
    if util.find_spec("numpy") is not None:
        import numpy
        print(f"[OK] numpy ({numpy.__version__}) - "
              f"Numerical computation ready")
    else:
        print("[KO] numpy - numpy could not be imported."
              " Use 'pip install numpy'")
    if util.find_spec("matplotlib") is not None:
        import matplotlib
        print(f"[OK] matplotlib ({metadata.version('matplotlib')}) - "
              f"Visualization ready")
    else:
        print("[KO] matplotlib - matplotlib could not be imported."
              " Use 'pip install matplotlib'")
    print()
    print("Analyzing Matrix data...")
    data_list = numpy.ndarray = numpy.random.rand(100, 10)
    print(f"Processing {len(data_list)} data points...")
    proc_data: pandas.
