import tkinter as tk
from tkinter import messagebox

from application.select_business import search_businesses
from infrastructure.config import downloads_dir, businesses_base_dir
from infrastructure.filesystem import get_two_latest_files
from infrastructure.xml_reader import extract_nf_data_from_xml
from application.organize_business import (
    get_nf_folder,
    get_year_folder,
    get_month_folder,
)
from application.process_business import process_business_files


class App(tk.Tk):
    """
    Main application window responsible for:
    - Searching businesses
    - Selecting the target business
    - Processing NF files (XML/PDF)
    """

    def __init__(self, conn):
        super().__init__()
        self.conn = conn

        self.title("Invoice Processor")
        self.geometry("400x500")
        self.resizable(False, False)

        # Search input
        self.search_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.search_var, font=("Arial", 12))
        self.entry.pack(pady=10, fill="x", padx=20)

        # Business list
        self.listbox = tk.Listbox(self, height=15)
        self.listbox.pack(fill="both", expand=True, padx=20)

        # Action button
        self.button = tk.Button(self, text="Process", command=self.process)
        self.button.pack(pady=10)

        # Update list whenever the search text changes
        self.search_var.trace_add("write", self.update_list)

    def update_list(self, *_):
        """
        Update the business list based on the search term.
        """
        term = self.search_var.get()

        self.listbox.delete(0, tk.END)

        # Avoid unnecessary queries
        if len(term) < 3:
            return

        results = search_businesses(self.conn, term)

        for business in results:
            self.listbox.insert(tk.END, business)

    def process(self):
        """
        Process the selected business:
        - Locate NF folders
        - Read the latest XML
        - Rename and move files
        """
        business = self.listbox.get(tk.ACTIVE)

        if not business:
            messagebox.showwarning("Warning", "Please select a business")
            return

        try:
            # Resolve target directories
            business_dir = businesses_base_dir() / business
            nf_dir = get_nf_folder(business_dir)
            year_dir = get_year_folder(nf_dir)
            month_dir = get_month_folder(year_dir)

            # Get latest downloaded files
            files = get_two_latest_files(downloads_dir())

            # Extract XML data
            xml_files = [f for f in files if f.suffix.lower() == ".xml"]
            if not xml_files:
                raise FileNotFoundError("No XML file found")

            info = extract_nf_data_from_xml(xml_files[0])

            # Rename and move files
            renamed_files = process_business_files(files, info, month_dir)

            filenames = "\n".join(file.name for file in renamed_files)

            messagebox.showinfo(
                "Success",
                f"Files processed successfully!\n\n"
                f"{filenames}\n\n"
                f"Destination:\n{month_dir}",
            )

        except Exception as error:
            messagebox.showerror("Error", str(error))
