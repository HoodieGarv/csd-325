"""
Garvin Stewart
Module 4.2 Assignment
4/20/2026

"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


FILENAME = 'sitka_weather_2018_simple.csv'


def load_weather_data():
    """
    Open the CSV file and extract dates, highs, and lows.
    Returns three lists: dates, highs, lows.
    """
    dates, highs, lows = [], [], []

    with open(FILENAME) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))   # TMAX column
            lows.append(int(row[6]))    # TMIN column

    return dates, highs, lows


def plot_highs(dates, highs):
    """Plot daily high temperatures in red."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def plot_lows(dates, lows):
    """Plot daily low temperatures in blue."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def display_menu():
    """Print the program menu to the console."""
    print("\n--- Sitka 2018 Weather Viewer ---")
    print("  H - View High Temperatures")
    print("  L - View Low Temperatures")
    print("  E - Exit")
    print("---------------------------------")


def main():
    """
    Main program loop.
    Load weather data once, then loop on the menu until the user exits.
    """
    print("Loading weather data...")
    dates, highs, lows = load_weather_data()
    print("Data loaded successfully.")

    while True:
        display_menu()
        choice = input("Enter your selection (H / L / E): ").strip().upper()

        if choice == 'H':
            print("Generating high temperature graph...")
            plot_highs(dates, highs)

        elif choice == 'L':
            print("Generating low temperature graph...")
            plot_lows(dates, lows)

        elif choice == 'E':
            print("\nThank you for using the Sitka Weather Viewer. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid selection. Please enter H, L, or E.")


if __name__ == '__main__':
    main()
