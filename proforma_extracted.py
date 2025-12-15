import pandas as pd
import camelot

tables = camelot.io.read_pdf(
    "Proforma_Invoice_2025-12-12.pdf",
    pages="all",
    flavor="lattice"
)

print("Tables found:", tables.n)


with pd.ExcelWriter("proforma_extracted.xlsx", engine="openpyxl") as writer:
    for i, table in enumerate(tables):
        df = table.df

        # Remove empty rows
        df = df[df.apply(lambda x: x.str.strip().ne('').any(), axis=1)]

        df.to_excel(
            writer,
            sheet_name=f"Table_{i+1}",
            index=False,
            header=False
        )

print("Excel file created successfully")





