import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print(f"{alchemy.create_air()}")
    print()
    try:
        print(f"{alchemy.create_earth()}")
    except Exception as e:
        print(e)
