from data.data_handler import load_data
from visuals.plotter import create_bar_chart

def main():
    data = load_data()

    create_bar_chart(data)

if __name__ == "__main__":
    main()