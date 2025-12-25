#!/usr/bin/env python3
"""
Example script demonstrating data manipulation with pandas.
Run: python scripts/data_example.py
"""

try:
    import pandas as pd
except ImportError:
    print("pandas not installed. Install packages with: pip install -r requirements.txt")
    exit(1)


def main():
    """Demonstrate basic pandas operations."""
    # Create sample data
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 28],
        'city': ['New York', 'San Francisco', 'Chicago', 'Boston']
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    print("Sample Data:")
    print(df)
    print(f"\nAverage age: {df['age'].mean():.1f}")
    print(f"\nPeople over 28:")
    print(df[df['age'] > 28])


if __name__ == "__main__":
    main()
