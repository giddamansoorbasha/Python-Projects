import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Dish": [
        "Chicken Chettinad", "Hyderabadi Biryani", "Andhra Chilli Chicken", "Kerala Chicken Roast", "Mangalorean Chicken Curry","Chicken 65", "Idli", "Dosa", "Vada", "Uttapam",
        "Pesarattu", "Ragi Mudde", "Kozhi Varuval", "Gongura Chicken", "Natu Kodi Pulusu",
        "Kappa Meen Curry", "Chettinad Fish Fry", "Chicken Sukka", "Appam", "Neer Dosa",
        "Puttu", "Upma", "Rasam", "Sambar", "Avial",
        "Paneer Dosa", "Mysore Masala Dosa", "Egg Dosa", "Kara Kuzhambu", "Vegetable Kurma"
    ],
    "Spice_Level": [9, 8, 10, 7, 8,9, 2, 3, 4, 3,5, 6, 9, 10, 8,7, 8, 9, 2, 3,3, 4, 6, 5, 4,5, 6, 7, 8, 5],
    "Popularity_Score": [85, 95, 80, 75, 70,90, 88, 92, 85, 80,78, 65, 82, 79, 76,70, 74, 83, 87, 89,84, 81, 77, 86, 79,83, 91, 88, 75, 80
    ]
}

df = pd.DataFrame(data)

x = list(df['Spice_Level'])
y = list(df['Popularity_Score'])

class RecommendFood:

    def __init__(self, user):
        self.x = x
        self.y = y
        self.user = user

    def euclidean(self, v1,v2):
        return sum((x-y)**2 for x,y in zip(v1,v2))**0.5

    def d(self, v,x,y):
        distances = [self.euclidean(v,[a,b]) for a,b in zip(x,y)]
        return distances
    
    def recommend(self):
        distances = [round(x,2) for x in self.d(self.user,self.x,self.y)]
        sorted_distances = sorted(distances)
        indexes = np.argsort(distances)[:5]
        dishes = [df.iloc[i]['Dish'] for i in indexes]
        return dishes
        
    def plot(self):
        plt.scatter(df['Spice_Level'], df['Popularity_Score'])
        plt.scatter(self.user[0], self.user[1], color='green', s=100, label='Your Choice')
        plt.legend()
        plt.title('Food Recommendation Visualization')
        plt.xlabel('Spice_Level')
        plt.ylabel('Popularity_Score')
        plt.show()

while True:
    print("\n---Welcome To Food Recommendation---\n")
    yes_no = input("Do you want me to recommend food? (Yes/No): ").strip().lower()
    if yes_no=="yes":
        print("\nTo recommend food, I need two parameters: \n\n1) Popularity_Score\n2) Spice_Level\n")
        p2 = float(input("Enter The Popularity Score (65-95): "))
        p1 = float(input("Enter The Spicy Level (2-10): "))
        food = RecommendFood(list((p1,p2)))
        while True:
            choice = int(input("\nChoose an option:\n1) Get Recommendation\n2) Plot the Graph\n3) Exit\n"))
            if choice==1:
                foods = food.recommend()
                print("\nTop Food Recommendations: \n")
                for i,f in enumerate(foods,start=1):
                    print(f"{i}) {f}")
            elif choice==2:
                food.plot()
                print("🟢 Is Your Data!.")
            elif choice==3:
                print("Thank You, Bye!")
                break
            else:
                print("Invalid Input!")
    elif yes_no=="no":
        print("Thank You, Bye!")
        break
    else:
        print("Invalid Input!")