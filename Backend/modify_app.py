import subprocess

def run_database_script():
    # Run the database script
    subprocess.run(["python", "databaseforapp.py"], check=True)

if __name__ == "__main__":
    # Run the database update script
    run_database_script()

    # Your main application logic here
    print("Running main application...")
    # Add your existing app logic here
