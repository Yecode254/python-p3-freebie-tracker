from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dev, Company

DATABASE_URL = "sqlite:///freebies.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def list_freebies_by_dev(dev_id):
    session = Session()
    freebies = Dev.get_freebies(session, dev_id)
    if freebies:
        print(f"Freebies for Dev ID {dev_id}:")
        for f in freebies:
            print(f" - {f.item_name} (${f.value}) from {f.company.name}")
        total = sum(f.value for f in freebies)
        print(f"Total value: ${total}")
    else:
        print("No freebies found or invalid dev ID.")
    session.close()

def list_freebies_by_company(company_id):
    session = Session()
    freebies = Company.get_freebies(session, company_id)
    if freebies:
        print(f"Freebies from Company ID {company_id}:")
        for f in freebies:
            print(f" - {f.item_name} (${f.value}) to {f.dev.name}")
        total = sum(f.value for f in freebies)
        print(f"Total value: ${total}")
    else:
        print("No freebies found or invalid company ID.")
    session.close()

def main():
    print("Choose an option:")
    print("1. List freebies by Dev ID")
    print("2. List freebies by Company ID")
    choice = input("Enter choice (1 or 2): ")
    if choice == '1':
        dev_id = int(input("Enter Dev ID: "))
        list_freebies_by_dev(dev_id)
    elif choice == '2':
        company_id = int(input("Enter Company ID: "))
        list_freebies_by_company(company_id)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
