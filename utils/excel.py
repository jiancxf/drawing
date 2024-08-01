import pandas as pd
import repository.sqlit as repo


# resolve excel file
def resolve_excel(file_path: str):
    df = pd.ExcelFile(file_path)
    # TODO here need to handle more complicate header
    for sheet_name in df.sheet_names:
        sheet = pd.read_excel(file_path, sheet_name=sheet_name)
        # create table for each sheet
        try:
            repo.create_table(sheet_name, list(sheet.columns))
            # import data into database
            data = []
            for row in sheet.values:
                data.append(tuple(row))
            repo.insert_data(sheet_name, list(sheet.columns), data)
        except Exception as e:
            raise e

