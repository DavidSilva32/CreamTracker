from data_manager import load_data, update_use, get_last_used

def main():
    creams = load_data()
    print(get_last_used(creams))

    new_cream_used = "gold cream"
    print(update_use(data=creams, new_cream_used=new_cream_used))

if __name__ == "__main__":
    main()