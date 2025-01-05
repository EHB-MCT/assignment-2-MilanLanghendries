import matplotlib.pyplot as plt

def create_bar_chart(data):
    """Creates a bar chart from the provided data."""
    categories = data.get("category", [])
    values = data.get("values", [])

    plt.bar(categories, values, color="skyblue")
    plt.title("Sample Data Visualization")
    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.show()