class PCBuild:
    def __init__(self, current_spent):
        self._current_spent = current_spent
        self._budget = None
        self._gpu_list = {
                "Radeon RX 6500 XT": 150,
                "Radeon RX 6600": 230,
                "Intel Arc A750": 250,
                "Intel Arc A770": 350,
                "RTX 4060 Ti": 399,
                "RTX 4070": 499,
                "RTX 4080": 699,
                "RTX 4090": 1499
                }
        self._mid_tier_gpu_list = {
                "Radeon RX 5500 XT": 199,
                "Radeon RX 5600 XT": 299,
                "GTX 1660 Super": 249,
                "GTX 1660 Ti": 279,
                }

    def get_current_spent(self):
        return self._current_spent

    def set_budget(self, budget):
        self._budget = budget

    def get_budget(self):
        return self._budget

    def get_gpu_list(self):
        return self._gpu_list

    def recommend_gpus(self, release_year, budget=None):
        if release_year <= 2011:
            recommended_gpus = []
            gpu_list = self._mid_tier_gpu_list
            if budget is not None:
                for gpu, price in gpu_list.items():
                    if price <= budget - self._current_spent:
                        recommended_gpus.append(gpu)
            else:
                recommended_gpus = list(gpu_list.keys())
        else:
            recommended_gpus = []
            gpu_list = self._gpu_list
            if self._budget is not None:
                for gpu, price in gpu_list.items():
                    if price <= self._budget - self._current_spent:
                        recommended_gpus.append(gpu)
            else:
                recommended_gpus = list(gpu_list.keys())
        return recommended_gpus

starting_spent = int(input("Hello, welcome to your PC build price calculator! Please enter your current amount spent on your PC build to get started: "))
assure_correct = input(f"You entered {starting_spent}, are you sure that is correct? Enter Y for yes and N for no. ")
if assure_correct == 'Y':
    print(f"Okay, you've currently spent {starting_spent}")
if assure_correct == 'N':
    starting_spent = int(input("Please enter a new amount: "))
release_year = int(input("Do you play games released before or after 2011? Enter 1 for before 2011 and 2 for after 2011: "))
if release_year == 1:
    print("Since you play games released before 2011, we recommend a mid-tier GPU to avoid overpaying for graphics power you don't need.")
    print("Now that you have your current amount spent setup, you can input your budget to get a list of recommended GPUs.")
    print("You can input your budget by entering 'set budget', you can view the recommended GPUs by entering 'view recommended GPUs', and you can view your current amount spent by entering 'show me my current spent'. Enter 'quit' to close the app.")
    while True:
        user_build = PCBuild(starting_spent)
        user_input = input("What would you like to do? ")
        if user_input == 'set budget':
            budget = int(input("What is your budget for your PC build? "))
            user_build.set_budget(budget)
            print(f"Your budget has been set to {budget}!")
        elif user_input == 'view recommended GPUs':
            recommended_gpus = PCBuild(starting_spent).recommend_gpus(release_year, user_build.get_budget())
            print(f"Here are the recommended mid-tier GPUs for your budget: {', '.join(recommended_gpus)}")

        elif user_build.get_budget() is None:
            print("Please set your budget first by entering 'set budget'.")
        else:
            recommended_gpus = user_build.recommend_gpus(release_year)
            if not recommended_gpus:
                print("Sorry, there are no GPUs that fall within your budget.")
            else:
                print(f"Recommended GPUs within your budget of {user_build.get_budget()} are: ")
                for gpu in recommended_gpus:
                    print(gpu)
        if user_input == 'quit':
            print("Thanks for using the app!")
            break
        elif user_input != 'show me my current spent' and user_input != 'set budget' and user_input != 'view recommended GPUs' and user_input != 'quit':
            print("I'm sorry, but that is not a valid response. Please choose a valid response such as show me my current spent, set budget, view recommended GPUs, or quit. ")

else:
    user_build = PCBuild(starting_spent)
    print("Now that you have your current amount spent setup, you can input your budget to get a list of recommended GPUs.")
    print("You can input your budget by entering 'set budget', you can view the recommended GPUs by entering 'view recommended GPUs', and you can view your current amount spent by entering 'show me my current spent'. Enter 'quit' to close the app.")

    while True:
        user_input = input("What would you like to do? ")
        if user_input == 'set budget':
            budget = int(input("What is your budget for your PC build? "))
            user_build.set_budget(budget)
            print(f"Your budget has been set to {budget}!")
        elif user_input == 'view recommended GPUs':
            print(user_build.get_gpu_list())
        if user_build.get_budget() is None:
            print("Please set your budget first by entering 'set budget'.")
        else:
            recommended_gpus = user_build.recommend_gpus(release_year)
            if not recommended_gpus:
                print("Sorry, there are no GPUs that fall within your budget.")
            else:
                print(f"Recommended GPUs within your budget of {user_build.get_budget()} are: ")
                for gpu in recommended_gpus:
                    print(gpu)
        if user_input == 'quit':
            print("Thanks for using the app!")
            break
        elif user_input != 'show me my current spent' and user_input != 'set budget' and user_input != 'view recommended GPUs' and user_input != 'quit':
            print("I'm sorry, but that is not a valid response. Please choose a valid response such as show me my current spent, set budget, view recommended GPUs, or quit. ")