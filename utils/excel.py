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


def export_to_excel(title: str, file_path: str, data: dict):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter(f"{file_path}\\{title}.xlsx")
    # 将DataFrame写入Excel中
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()


def table_list_to_dict(columns: list, dataList: list) -> dict:
    result = dict()
    key_dict = dict()
    for idx, column in enumerate(columns):
        key_dict[idx] = column
        result[column] = []
    for data in dataList:
        for idx, value in enumerate(data):
            result[key_dict[idx]].append(value)
    return result


