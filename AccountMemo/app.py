import logic.view_ctr as view
import logic.db_ctr as db


def main():
    db.start_mydb()
    view.open_top()

if __name__ == "__main__":
    main()