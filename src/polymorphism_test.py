from nascar_data import NASCARData
from f1_data import F1Data
from indycar_data import IndyCarData

def show_scores():
    """
    Create different race objects and print their scores.

    This shows polymorphism: same method name, different results.
    """
    races = [
        NASCARData("Daytona", 200),
        F1Data("Monaco", 78),
        IndyCarData("Indy 500", 200)
    ]

    for r in races:
        print(f"Race type: {type(r).__name__}")
        print("Performance score:", r.compute_performance_score())
        print("-----")

if __name__ == "__main__":
    show_scores()