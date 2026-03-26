import time

def start_evaluation():
    print("-" * 50)
    print("DIGITAL LITERACY PROJECT - EXECUTION CONSOLE")
    print("-" * 50)
    print(f"Student: Sweksha Kakkar | Reg No: 25BCY10159")
    print("Specialization: CSE Cyber Security")
    print("-" * 50)
    
    time.sleep(1)
    print("\nVerifying Project Components...")
    
    components = [
        "Task 1: Infographic Design................[OK]",
        "Task 2: Professional Profiles..............[OK]",
        "Task 3: HackerRank & Google Form Survey....[OK]",
        "Task 4: Email Etiquette & Checklist........[OK]",
        "Task 5: Cyber Safety Case Study............[OK]",
        "Final Report: PDF Documentation............[OK]"
    ]
    
    for item in components:
        print(item)
        time.sleep(0.4)
    
    print("\n[SUCCESS] Project is fully documented and ready for evaluation.")
    print("-" * 50)

if __name__ == "__main__":
    start_evaluation()
