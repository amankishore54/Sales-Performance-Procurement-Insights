Sales Performance & Procurement Insights

This project delivers an end-to-end Business Intelligence solution designed to support commercial decision-making and procurement control. The objective was not only to visualize data, but to build a reporting experience that answers why performance looks the way it does and where operational risks require attention.

The solution is structured into two clear business use cases: 
1. Sales Performance – understanding revenue trends, growth drivers, and distribution effectiveness. 
2. Procurement Control – identifying mismatches between ordered and invoiced quantities and values through exception-based monitoring.

Data Architecture & Flow

Sales Data
• Sales transactions were stored in a SQLite database to represent a lightweight transactional data source.
• Power BI connects to SQLite via ODBC drivers, enabling direct querying and refresh.
• Initial data quality checks and corrections were applied in Power Query before modeling.

Procurement Data
• Purchase Order and Invoice documents were provided as PDFs.
• Camelot and Pandas were used to extract structured tables from machine-generated PDFs.
• Extracted data was exported to Excel and then ingested into Power BI for analysis.

Tooling & Technology 

The following tools were selected intentionally based on use case fit:
• SQLite – Lightweight, file-based storage suitable for local transactional analysis.
• ODBC Connector – Enables standardized connectivity between SQLite and Power BI.
• Power BI – Used for data modeling, metric definition (DAX), and interactive reporting.
• Camelot & Pandas – Reliable open-source tools for extracting and transforming tabular data from PDFs.
• Excel – Served as an intermediate, structured format for procurement data ingestion.

Key Metrics & KPIs

Sales Performance

•Total Sales
•Year-over-Year (YoY) Growth %
•Active Stores
•Average Sales per Store

Procurement Control

•Ordered Quantity
•Invoiced Quantity
•Quantity Variance %
•Value Variance %

How to Run the Project

1. Open the Power BI (.pbix) file.
2. Verify the SQLite database file path in the data source settings.
3. Refresh all data sources.
4. Use the homepage navigation to explore the dashboards.

