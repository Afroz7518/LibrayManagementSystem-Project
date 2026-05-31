from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import re
import os

# ─────────────────────────────────────────────────────────────────────────────
# Database helpers
# ─────────────────────────────────────────────────────────────────────────────

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library.db")

def create_db():
    """Create the SQLite database and the library table if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS library (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            membertype    TEXT    NOT NULL,
            prnno         TEXT    NOT NULL,
            idno          TEXT    NOT NULL,
            firstname     TEXT    NOT NULL,
            lastname      TEXT    NOT NULL,
            address       TEXT,
            pincode       TEXT,
            mobile        TEXT,
            bookid        TEXT    NOT NULL,
            booktitle     TEXT    NOT NULL,
            bookauthor    TEXT,
            issuedate     TEXT    NOT NULL,
            duedate       TEXT    NOT NULL,
            latereturnfine TEXT,
            actualprice   TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_PATH)


# ─────────────────────────────────────────────────────────────────────────────
# Main Application
# ─────────────────────────────────────────────────────────────────────────────

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x810")
        self.root.minsize(1200, 750)
        self.root.configure(bg="powder blue")

        # ── String variables ──────────────────────────────────────────────
        self.member_var        = StringVar()
        self.prn_no_var        = StringVar()
        self.idno_var          = StringVar()
        self.firstname_var     = StringVar()
        self.lastname_var      = StringVar()
        self.address_var       = StringVar()
        self.pincode_var       = StringVar()
        self.mobile_var        = StringVar()
        self.bookid_var        = StringVar()
        self.booktitle_var     = StringVar()
        self.bookauthor_var    = StringVar()
        self.issuedate_var     = StringVar()
        self.duedate_var       = StringVar()
        self.latereturnfine_var = StringVar()
        self.actualprice_var   = StringVar()
        self.search_by_var     = StringVar()
        self.search_txt_var    = StringVar()

        # Tracks the DB row-id of the currently selected treeview item
        self._selected_row_id = None

        self._build_ui()
        self.show_data()  # populate table on startup

        # Key bindings
        self.root.bind("<Escape>", lambda e: self.reset_data())

    # ─────────────────────────────────────────────────────────────────────
    # UI Construction
    # ─────────────────────────────────────────────────────────────────────

    def _build_ui(self):
        # ── Title ──────────────────────────────────────────────────────────
        lbl_title = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            bg="powder blue", fg="black",
            bd=20, relief=RIDGE,
            font=("times new roman", 40, "bold"),
            padx=2, pady=6
        )
        lbl_title.pack(side=TOP, fill=X)

        # ── Data entry frame ───────────────────────────────────────────────
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=120, width=1530, height=400)

        # Left panel — member + book fields
        DataFrameLeft = LabelFrame(
            frame,
            text="Library Membership Information",
            bg="powder blue", fg="green",
            bd=12, relief=RIDGE,
            font=("times new roman", 15, "bold")
        )
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # ── Left panel widgets ─────────────────────────────────────────────
        lbl_cfg = dict(bg="powder blue", font=("times new roman", 14, "bold"), padx=2, pady=5)
        ent_cfg = dict(font=("times new roman", 14, "bold"), width=22)

        # Row 0 – Member type
        Label(DataFrameLeft, text="Member Type:", **lbl_cfg).grid(row=0, column=0, sticky=W)
        com_member = ttk.Combobox(
            DataFrameLeft,
            textvariable=self.member_var,
            font=("times new roman", 12, "bold"),
            width=27, state="readonly"
        )
        com_member["values"] = ("Admin staff", "Student", "Lecturer")
        com_member.current(0)
        com_member.grid(row=0, column=1)

        # Row 1 – PRN No
        Label(DataFrameLeft, text="PRN NO:", **lbl_cfg).grid(row=1, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.prn_no_var, **ent_cfg).grid(row=1, column=1)

        # Row 2 – ID No
        Label(DataFrameLeft, text="ID NO:", **lbl_cfg).grid(row=2, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.idno_var, **ent_cfg).grid(row=2, column=1)

        # Row 3 – First Name
        Label(DataFrameLeft, text="First Name:", **lbl_cfg).grid(row=3, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.firstname_var, **ent_cfg).grid(row=3, column=1)

        # Row 4 – Last Name
        Label(DataFrameLeft, text="Last Name:", **lbl_cfg).grid(row=4, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.lastname_var, **ent_cfg).grid(row=4, column=1)

        # Row 5 – Address
        Label(DataFrameLeft, text="Address:", **lbl_cfg).grid(row=5, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.address_var, **ent_cfg).grid(row=5, column=1)

        # Row 6 – Pin Code
        Label(DataFrameLeft, text="PinCode:", **lbl_cfg).grid(row=6, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.pincode_var, **ent_cfg).grid(row=6, column=1)

        # Row 7 – Mobile
        Label(DataFrameLeft, text="Mobile:", **lbl_cfg).grid(row=7, column=0, sticky=W)
        Entry(DataFrameLeft, textvariable=self.mobile_var, **ent_cfg).grid(row=7, column=1)

        # Right side of left panel — book info
        # Row 0 – Book ID
        Label(DataFrameLeft, text="Book ID:", **lbl_cfg).grid(row=0, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.bookid_var, **ent_cfg).grid(row=0, column=3)

        # Row 1 – Book Title
        Label(DataFrameLeft, text="Book Title:", **lbl_cfg).grid(row=1, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.booktitle_var, **ent_cfg).grid(row=1, column=3)

        # Row 2 – Book Author
        Label(DataFrameLeft, text="Book Author:", **lbl_cfg).grid(row=2, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.bookauthor_var, **ent_cfg).grid(row=2, column=3)

        # Row 3 – Issue Date
        Label(DataFrameLeft, text="Issue Date:", **lbl_cfg).grid(row=3, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.issuedate_var, **ent_cfg).grid(row=3, column=3)

        # Row 4 – Due Date
        Label(DataFrameLeft, text="Due Date:", **lbl_cfg).grid(row=4, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.duedate_var, **ent_cfg).grid(row=4, column=3)

        # Row 5 – Late Return Fine
        Label(DataFrameLeft, text="Late Return Fine:", **lbl_cfg).grid(row=5, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.latereturnfine_var, **ent_cfg).grid(row=5, column=3)

        # Row 6 – Actual Price
        Label(DataFrameLeft, text="Actual Price:", **lbl_cfg).grid(row=6, column=2, sticky=W)
        Entry(DataFrameLeft, textvariable=self.actualprice_var, **ent_cfg).grid(row=6, column=3)

        # ── Right panel — book list ────────────────────────────────────────
        DataFrameRight = LabelFrame(
            frame,
            text="Book List  (double-click to select)",
            bg="powder blue", fg="green",
            bd=12, relief=RIDGE,
            font=("times new roman", 12, "bold")
        )
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        list_scrollbar = Scrollbar(DataFrameRight)
        list_scrollbar.grid(row=0, column=1, sticky="ns")

        list_books = [
            "Python Programming", "Data Structure in C", "Operating System",
            "Computer Architecture", "Digital Signal & Telecom Labs", "Electronics",
            "Mechanics", "The Secret of Millionaire Mind", "Pride and Prejudice",
            "The Lord of the Rings", "Harry Potter", "Jane Eyre", "Java",
            "Automata Theory", "Internet of Things", "Machine Learning",
            "Super Intelligence", "Deep Learning", "Human Capability",
            "The Alignment Problem", "Control System", "The Art of Electronics",
            "Digital Electronics", "Theory of Automata", "Law of Attraction",
            "OOP Concepts", "Programming in C", "General Aptitude", "Reasoning",
            "General Knowledge", "The Secret of Happiness", "Chemistry",
            "Physics", "Mathematics", "Poem Books", "Social Science",
            "Political Science",
        ]

        self.listBox = Listbox(
            DataFrameRight,
            font=("times new roman", 12, "bold"),
            width=20, height=16,
            selectbackground="#2d7dd2",
            selectforeground="white"
        )
        self.listBox.grid(row=0, column=0, padx=4)
        list_scrollbar.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=list_scrollbar.set)

        for item in list_books:
            self.listBox.insert(END, item)

        # Double-click on book list fills Book Title
        self.listBox.bind("<Double-Button-1>", self._on_book_select)

        # ── Button frame ───────────────────────────────────────────────────
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=520, width=1530, height=100)

        btn_cfg = dict(font=("times new roman", 12, "bold"), width=20)
        search_btn_cfg = dict(font=("times new roman", 12, "bold"), width=14)

        Button(Framebutton, text="Add Data",  bg="#2196F3", fg="white",
               command=self.add_data,    **btn_cfg).grid(row=0, column=0, padx=6, pady=8)
        Button(Framebutton, text="Show Data", bg="#4CAF50", fg="white",
               command=self.show_data,   **btn_cfg).grid(row=0, column=1, padx=6, pady=8)
        Button(Framebutton, text="Update",    bg="#FF9800", fg="white",
               command=self.update_data, **btn_cfg).grid(row=0, column=2, padx=6, pady=8)
        Button(Framebutton, text="Delete",    bg="#F44336", fg="white",
               command=self.delete_data, **btn_cfg).grid(row=0, column=3, padx=6, pady=8)
        Button(Framebutton, text="Reset",     bg="#9C27B0", fg="white",
               command=self.reset_data,  **btn_cfg).grid(row=0, column=4, padx=6, pady=8)
        Button(Framebutton, text="Exit",      bg="#607D8B", fg="white",
               command=self.exit_app,    **btn_cfg).grid(row=0, column=5, padx=6, pady=8)


        # ── Details / treeview frame ───────────────────────────────────────
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        cols = (
            "membertype", "prnno", "idno", "firstname", "lastname",
            "address", "pincode", "mobile", "bookid", "booktitle",
            "bookauthor", "issuedate", "duedate", "latereturnfine", "actualprice"
        )
        self.library_table = ttk.Treeview(
            Table_frame,
            columns=cols,
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set
        )

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT,  fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        headings = {
            "membertype":    "Member Type",
            "prnno":         "PRN NO",
            "idno":          "ID NO",
            "firstname":     "First Name",
            "lastname":      "Last Name",
            "address":       "Address",
            "pincode":       "Pin Code",
            "mobile":        "Mobile",
            "bookid":        "Book ID",
            "booktitle":     "Book Title",
            "bookauthor":    "Book Author",
            "issuedate":     "Issue Date",
            "duedate":       "Due Date",
            "latereturnfine":"Late Return Fine",
            "actualprice":   "Actual Price",
        }
        for col, heading in headings.items():
            self.library_table.heading(col, text=heading)
            self.library_table.column(col, width=110, anchor=CENTER)

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        # Click on treeview row → populate form
        self.library_table.bind("<<TreeviewSelect>>", self._on_row_select)

    # ─────────────────────────────────────────────────────────────────────
    # Validation
    # ─────────────────────────────────────────────────────────────────────

    def _validate(self):
        """Return (True, None) on success or (False, error_message) on failure."""
        required = {
            "Member Type":  self.member_var.get().strip(),
            "PRN NO":       self.prn_no_var.get().strip(),
            "ID NO":        self.idno_var.get().strip(),
            "First Name":   self.firstname_var.get().strip(),
            "Last Name":    self.lastname_var.get().strip(),
            "Book ID":      self.bookid_var.get().strip(),
            "Book Title":   self.booktitle_var.get().strip(),
            "Issue Date":   self.issuedate_var.get().strip(),
            "Due Date":     self.duedate_var.get().strip(),
        }
        for label, value in required.items():
            if not value:
                return False, f"'{label}' is required."

        # Date format DD/MM/YYYY
        date_re = re.compile(r"^\d{2}/\d{2}/\d{4}$")
        for date_field in ("Issue Date", "Due Date"):
            val = required[date_field]
            if not date_re.match(val):
                return False, f"'{date_field}' must be in DD/MM/YYYY format.\nGot: '{val}'"

        # Mobile — optional but if provided must be 10 digits
        mobile = self.mobile_var.get().strip()
        if mobile and not re.fullmatch(r"\d{10}", mobile):
            return False, "Mobile number must be exactly 10 digits."

        # Pin code — optional but if provided must be 6 digits
        pincode = self.pincode_var.get().strip()
        if pincode and not re.fullmatch(r"\d{6}", pincode):
            return False, "Pin code must be exactly 6 digits."

        # Fine & Price — optional but must be numeric if provided
        for label, var in [("Late Return Fine", self.latereturnfine_var),
                           ("Actual Price",      self.actualprice_var)]:
            val = var.get().strip()
            if val:
                try:
                    float(val)
                except ValueError:
                    return False, f"'{label}' must be a numeric value."

        return True, None

    # ─────────────────────────────────────────────────────────────────────
    # Helper — collect form values as a tuple (without id)
    # ─────────────────────────────────────────────────────────────────────

    def _form_values(self):
        return (
            self.member_var.get().strip(),
            self.prn_no_var.get().strip(),
            self.idno_var.get().strip(),
            self.firstname_var.get().strip(),
            self.lastname_var.get().strip(),
            self.address_var.get().strip(),
            self.pincode_var.get().strip(),
            self.mobile_var.get().strip(),
            self.bookid_var.get().strip(),
            self.booktitle_var.get().strip(),
            self.bookauthor_var.get().strip(),
            self.issuedate_var.get().strip(),
            self.duedate_var.get().strip(),
            self.latereturnfine_var.get().strip(),
            self.actualprice_var.get().strip(),
        )

    # ─────────────────────────────────────────────────────────────────────
    # Button handlers
    # ─────────────────────────────────────────────────────────────────────

    def add_data(self):
        ok, err = self._validate()
        if not ok:
            messagebox.showerror("Validation Error", err)
            return

        values = self._form_values()
        try:
            with get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO library
                        (membertype, prnno, idno, firstname, lastname, address,
                         pincode, mobile, bookid, booktitle, bookauthor,
                         issuedate, duedate, latereturnfine, actualprice)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, values)
            messagebox.showinfo("Success", "Record added successfully!")
            self.show_data()
            self.reset_data()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def show_data(self, where_clause=None, params=()):
        """Fetch rows from DB and refresh the treeview."""
        for row in self.library_table.get_children():
            self.library_table.delete(row)

        try:
            with get_connection() as conn:
                cur = conn.cursor()
                sql = """
                    SELECT membertype, prnno, idno, firstname, lastname, address,
                           pincode, mobile, bookid, booktitle, bookauthor,
                           issuedate, duedate, latereturnfine, actualprice, id
                    FROM library
                """
                if where_clause:
                    sql += f" WHERE {where_clause}"
                sql += " ORDER BY id ASC"
                cur.execute(sql, params)
                rows = cur.fetchall()

            for row in rows:
                db_id = row[-1]
                display_vals = row[:-1]
                self.library_table.insert("", END, iid=str(db_id), values=display_vals)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def search_data(self):
        """Search records by the selected field and refresh the treeview."""
        search_text = self.search_txt_var.get().strip()
        if not search_text:
            messagebox.showwarning("Search Required", "Please enter a search term.")
            return

        field_map = {
            "PRN NO": "prnno",
            "ID NO": "idno",
            "Book Title": "booktitle",
            "Member Type": "membertype",
        }
        search_field = field_map.get(self.search_by_var.get())
        if not search_field:
            messagebox.showerror("Search Error", "Invalid search field selected.")
            return

        where_clause = f"{search_field} LIKE ?"
        params = (f"%{search_text}%",)
        self.show_data(where_clause=where_clause, params=params)

    def _show_all_data(self):
        self.search_txt_var.set("")
        self.show_data()

    def update_data(self):
        if self._selected_row_id is None:
            messagebox.showwarning("No Selection", "Please click a row in the table to select it first.")
            return

        ok, err = self._validate()
        if not ok:
            messagebox.showerror("Validation Error", err)
            return

        values = self._form_values()
        try:
            with get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""
                    UPDATE library SET
                        membertype=?, prnno=?, idno=?, firstname=?, lastname=?,
                        address=?, pincode=?, mobile=?, bookid=?, booktitle=?,
                        bookauthor=?, issuedate=?, duedate=?, latereturnfine=?,
                        actualprice=?
                    WHERE id=?
                """, (*values, self._selected_row_id))
            messagebox.showinfo("Success", "Record updated successfully!")
            self._selected_row_id = None
            self.show_data()
            self.reset_data()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_data(self):
        if self._selected_row_id is None:
            messagebox.showwarning("No Selection", "Please click a row in the table to select it first.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this record?\nThis action cannot be undone."
        )
        if not confirm:
            return

        try:
            with get_connection() as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM library WHERE id=?", (self._selected_row_id,))
            messagebox.showinfo("Deleted", "Record deleted successfully!")
            self._selected_row_id = None
            self.show_data()
            self.reset_data()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def reset_data(self):
        """Clear all form fields and deselect any treeview row."""
        self.member_var.set("Admin staff")
        self.prn_no_var.set("")
        self.idno_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.pincode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.bookauthor_var.set("")
        self.issuedate_var.set("")
        self.duedate_var.set("")
        self.latereturnfine_var.set("")
        self.actualprice_var.set("")
        self._selected_row_id = None
        # Deselect any highlighted treeview row
        for item in self.library_table.selection():
            self.library_table.selection_remove(item)

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    # ─────────────────────────────────────────────────────────────────────
    # Interaction handlers
    # ─────────────────────────────────────────────────────────────────────

    def _on_row_select(self, event):
        """Populate form fields when a treeview row is clicked."""
        selected = self.library_table.selection()
        if not selected:
            return
        iid = selected[0]
        self._selected_row_id = int(iid)
        row = self.library_table.item(iid, "values")
        # row order matches the SELECT order in show_data
        self.member_var.set(row[0])
        self.prn_no_var.set(row[1])
        self.idno_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address_var.set(row[5])
        self.pincode_var.set(row[6])
        self.mobile_var.set(row[7])
        self.bookid_var.set(row[8])
        self.booktitle_var.set(row[9])
        self.bookauthor_var.set(row[10])
        self.issuedate_var.set(row[11])
        self.duedate_var.set(row[12])
        self.latereturnfine_var.set(row[13])
        self.actualprice_var.set(row[14])

    def _on_book_select(self, event):
        """Double-click on book list fills the Book Title field."""
        selection = self.listBox.curselection()
        if selection:
            title = self.listBox.get(selection[0])
            self.booktitle_var.set(title)


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    create_db()
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
