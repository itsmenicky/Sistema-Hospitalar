from database import init_db
from view import menu_principal

def main():
    init_db()
    menu_principal()

main()