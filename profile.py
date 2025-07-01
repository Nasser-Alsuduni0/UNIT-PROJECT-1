from rich.console import Console

def create_user_profile():
    console = Console()
    console.print("[bold green]Let's create your FitTrack profile![/bold green]")
    name = input("Enter your name: ").strip()
    while True:
        weight = input("Enter your weight (kg): ").strip()
        try:
            weight = float(weight)
            if weight > 0:
                break
            else:
                print("Please enter a positive number for weight.")
        except ValueError:
            print("Please enter a valid number for weight.")
    while True:
        height = input("Enter your height (cm): ").strip()
        try:
            height = float(height)
            if height > 0:
                break
            else:
                print("Please enter a positive number for height.")
        except ValueError:
            print("Please enter a valid number for height.")
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    console.print(f"[bold cyan]Welcome, {name}! Weight: {weight} kg, Height: {height} cm[/bold cyan]")
    console.print(f"[bold yellow]Your current BMI is: {bmi:.2f}[/bold yellow]")
    
    if bmi < 18.5:
        bmi_msg = "Underweight: BMI less than 18.5. You may need to gain weight for optimal health."
    elif 18.5 <= bmi < 25:
        bmi_msg = "Normal weight: BMI between 18.5 and 24.9. You are in a healthy range."
    elif 25 <= bmi < 30:
        bmi_msg = "Overweight: BMI between 25 and 29.9. You may need to lose weight for better health."
    else:
        bmi_msg = "Obese: BMI 30 or higher. It's important to consult with a healthcare provider."
    console.print(f"[bold magenta]{bmi_msg}[/bold magenta]")
    return {"name": name, "weight": weight, "height": height, "bmi": bmi} 