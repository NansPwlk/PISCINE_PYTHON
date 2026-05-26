import importlib.util
from importlib.metadata import version
import sys


def is_that_here() -> None:
    missing: bool = False
    required_list: list = ["numpy", "pandas", "matplotlib"]
    for elements in required_list:
        if not importlib.util.find_spec(elements):
            print("!!! MISSING MODULE !!!")
            print(f"{elements} is missing.\n")
            missing = True
    if missing:
        print("Please, chose between this two commands to properly install:")
        print("pip install -r requirements.txt")
        print("poetry install")
        sys.exit(1)
    else:
        print("LOADING STATUS: Loading programs...")
        print("Checking dependencies:")
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
        print(f"[OK] numpy ({version('numpy')}) - Numerical computation read")
        print(f"[OK] matplotlib ({version('matplotlib')}) "
              "- Visualization ready")


def create_matrix() -> None:
    import numpy  # type: ignore # noqa: E402
    import pandas  # type: ignore # noqa: E402
    import matplotlib.pyplot  # type: ignore # noqa: E402
    print("Processing 1000 data points...")
    data = numpy.random.randint(0, 100, 1000)
    data_tab = pandas.DataFrame(data, columns=["Matrix_Depth"])
    print("Generating visualization...")
    matplotlib.pyplot.plot(data_tab["Matrix_Depth"])
    matplotlib.pyplot.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    is_that_here()
    print("\nAnalyzing Matrix data...")
    create_matrix()


if __name__ == "__main__":
    main()
