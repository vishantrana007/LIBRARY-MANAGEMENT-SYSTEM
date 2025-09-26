# src/app.py

"""
Library Management System (Python + MySQL)
------------------------------------------
Features:
- Manage Books (Add, View, Update, Search, Delete)
- Manage Members (Add, View, Update, Search, Delete)
- Issue/Return Books with validations
- Track Issued & Returned books
- CLI-based user interface
"""

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from datetime import date

# Load environment variables
load_dotenv()


# ------------------- DB Connection -------------------
def get_connection():
    """Establish MySQL database connection."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except Error as e:
        print("❌ Error connecting to DB:", e)
        return None


# =====================================================
# 📚 BOOKS MODULE
# =====================================================
def add_book():
    """Add a new book record."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        qty = input("Enter quantity: ")

        if not qty.isdigit() or int(qty) <= 0:
            print("❌ Quantity must be a positive number.")
            return

        try:
            cursor.execute(
                "INSERT INTO books (title, author, qty) VALUES (%s, %s, %s)",
                (title, author, int(qty))
            )
            conn.commit()
            print("✅ Book added successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def view_books():
    """View all books."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            print("\n--- Books List ---")
            if rows:
                for row in rows:
                    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Qty: {row[3]}")
            else:
                print("No books available.")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def update_book():
    """Update book details."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        book_id = input("Enter Book ID to update: ")

        # Check if book exists
        cursor.execute("SELECT * FROM books WHERE book_id=%s", (book_id,))
        if not cursor.fetchone():
            print("❌ Book not found.")
            return

        title = input("Enter new title: ")
        author = input("Enter new author: ")
        qty = input("Enter new quantity: ")

        try:
            cursor.execute(
                "UPDATE books SET title=%s, author=%s, qty=%s WHERE book_id=%s",
                (title, author, qty, book_id)
            )
            conn.commit()
            print("✅ Book updated successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def search_books():
    """Search books by title or author."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        keyword = input("Enter book title or author to search: ")
        try:
            cursor.execute(
                "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s",
                (f"%{keyword}%", f"%{keyword}%")
            )
            rows = cursor.fetchall()
            print("\n--- Search Results ---")
            if rows:
                for row in rows:
                    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Qty: {row[3]}")
            else:
                print("❌ No books found.")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def delete_book():
    """Delete a book record."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        book_id = input("Enter Book ID to delete: ")

        # Validate existence
        cursor.execute("SELECT * FROM books WHERE book_id=%s", (book_id,))
        if not cursor.fetchone():
            print("❌ Book not found.")
            return

        try:
            cursor.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
            conn.commit()
            print("✅ Book deleted successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


# =====================================================
# 👤 MEMBERS MODULE
# =====================================================
def add_member():
    """Add a new member."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        name = input("Enter member name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        try:
            cursor.execute(
                "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)",
                (name, email, phone)
            )
            conn.commit()
            print("✅ Member added successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def view_members():
    """View all members."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM members")
            rows = cursor.fetchall()
            print("\n--- Members List ---")
            if rows:
                for row in rows:
                    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")
            else:
                print("No members found.")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def update_member():
    """Update member details."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        member_id = input("Enter Member ID to update: ")

        cursor.execute("SELECT * FROM members WHERE member_id=%s", (member_id,))
        if not cursor.fetchone():
            print("❌ Member not found.")
            return

        name = input("Enter new name: ")
        email = input("Enter new email: ")
        phone = input("Enter new phone number: ")

        try:
            cursor.execute(
                "UPDATE members SET name=%s, email=%s, phone=%s WHERE member_id=%s",
                (name, email, phone, member_id)
            )
            conn.commit()
            print("✅ Member updated successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def search_members():
    """Search members by name or email."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        keyword = input("Enter member name or email to search: ")
        try:
            cursor.execute(
                "SELECT * FROM members WHERE name LIKE %s OR email LIKE %s",
                (f"%{keyword}%", f"%{keyword}%")
            )
            rows = cursor.fetchall()
            print("\n--- Search Results ---")
            if rows:
                for row in rows:
                    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")
            else:
                print("❌ No members found.")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def delete_member():
    """Delete a member record."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        member_id = input("Enter Member ID to delete: ")

        cursor.execute("SELECT * FROM members WHERE member_id=%s", (member_id,))
        if not cursor.fetchone():
            print("❌ Member not found.")
            return

        try:
            cursor.execute("DELETE FROM members WHERE member_id=%s", (member_id,))
            conn.commit()
            print("✅ Member deleted successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


# =====================================================
# 📖 ISSUE / RETURN MODULE
# =====================================================
def issue_book():
    """Issue a book to a member."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        book_id = input("Enter Book ID to issue: ")
        member_id = input("Enter Member ID: ")
        issue_date = date.today()

        # Check availability
        cursor.execute("SELECT qty FROM books WHERE book_id=%s", (book_id,))
        result = cursor.fetchone()
        if not result:
            print("❌ Book not found.")
            return
        if result[0] <= 0:
            print("❌ Book is out of stock.")
            return

        try:
            cursor.execute(
                "INSERT INTO issue_books (book_id, member_id, issue_date) VALUES (%s, %s, %s)",
                (book_id, member_id, issue_date)
            )
            cursor.execute("UPDATE books SET qty = qty - 1 WHERE book_id=%s", (book_id,))
            conn.commit()
            print("✅ Book issued successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def return_book():
    """Return a book."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        issue_id = input("Enter Issue ID to return: ")
        return_date = date.today()

        # Check if issue record exists and not already returned
        cursor.execute("SELECT book_id, return_date FROM issue_books WHERE issue_id=%s", (issue_id,))
        record = cursor.fetchone()
        if not record:
            print("❌ Issue record not found.")
            return
        if record[1]:
            print("❌ Book already returned.")
            return

        try:
            cursor.execute("UPDATE issue_books SET return_date=%s WHERE issue_id=%s", (return_date, issue_id))
            cursor.execute("UPDATE books SET qty = qty + 1 WHERE book_id=%s", (record[0],))
            conn.commit()
            print("✅ Book returned successfully!")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def view_issued_books():
    """View all issued books (including not returned)."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT i.issue_id, b.title, m.name, i.issue_date, i.return_date
                FROM issue_books i
                JOIN books b ON i.book_id=b.book_id
                JOIN members m ON i.member_id=m.member_id
                """
            )
            rows = cursor.fetchall()
            print("\n--- Issued Books ---")
            if rows:
                for row in rows:
                    status = "Returned" if row[4] else "Not Returned"
                    print(f"Issue ID: {row[0]}, Book: {row[1]}, Member: {row[2]}, "
                          f"Issue Date: {row[3]}, Return Date: {row[4]}, Status: {status}")
            else:
                print("No issued books found.")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


def view_returned_books():
    """View all returned books."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT i.issue_id, b.title, m.name, i.issue_date, i.return_date
                FROM issue_books i
                JOIN books b ON i.book_id=b.book_id
                JOIN members m ON i.member_id=m.member_id
                WHERE i.return_date IS NOT NULL
                """
            )
            rows = cursor.fetchall()
            print("\n--- Returned Books ---")
            if rows:
                for row in rows:
                    print(f"Issue ID: {row[0]}, Book: {row[1]}, Member: {row[2]}, "
                          f"Issue Date: {row[3]}, Return Date: {row[4]}")
            else:
                print("No returned books found.")
        except Error as e:
            print("❌ Error:", e)
        finally:
            cursor.close()
            conn.close()


# =====================================================
# 🏠 MAIN MENU
# =====================================================
def main_menu():
    print("\n=== Library Management System ===")
    print("1. Manage Books")
    print("2. Manage Members")
    print("3. Issue / View Issued Books")
    print("4. Return / View Returned Books")
    print("5. Exit")
    return input("Enter your choice: ")


def run():
    """Main program loop."""
    while True:
        choice = main_menu()

        # Books
        if choice == '1':
            while True:
                print("\n📚 Manage Books")
                print("1. Add Book")
                print("2. View Books")
                print("3. Update Book")
                print("4. Search Books")
                print("5. Delete Book")
                print("6. Back to Main Menu")
                sub_choice = input("Enter choice: ")
                if sub_choice == '1': add_book()
                elif sub_choice == '2': view_books()
                elif sub_choice == '3': update_book()
                elif sub_choice == '4': search_books()
                elif sub_choice == '5': delete_book()
                elif sub_choice == '6': break
                else: print("❌ Invalid choice.")

        # Members
        elif choice == '2':
            while True:
                print("\n👤 Manage Members")
                print("1. Add Member")
                print("2. View Members")
                print("3. Update Member")
                print("4. Search Members")
                print("5. Delete Member")
                print("6. Back to Main Menu")
                sub_choice = input("Enter choice: ")
                if sub_choice == '1': add_member()
                elif sub_choice == '2': view_members()
                elif sub_choice == '3': update_member()
                elif sub_choice == '4': search_members()
                elif sub_choice == '5': delete_member()
                elif sub_choice == '6': break
                else: print("❌ Invalid choice.")

        # Issue
        elif choice == '3':
            while True:
                print("\n📖 Issue / View Issued Books")
                print("1. Issue a Book")
                print("2. View Issued Books")
                print("3. Back to Main Menu")
                sub_choice = input("Enter choice: ")
                if sub_choice == '1': issue_book()
                elif sub_choice == '2': view_issued_books()
                elif sub_choice == '3': break
                else: print("❌ Invalid choice.")

        # Return
        elif choice == '4':
            while True:
                print("\n🔄 Return / View Returned Books")
                print("1. Return a Book")
                print("2. View Returned Books")
                print("3. Back to Main Menu")
                sub_choice = input("Enter choice: ")
                if sub_choice == '1': return_book()
                elif sub_choice == '2': view_returned_books()
                elif sub_choice == '3': break
                else: print("❌ Invalid choice.")

        # Exit
        elif choice == '5':
            print("Exiting... Bye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    run()
