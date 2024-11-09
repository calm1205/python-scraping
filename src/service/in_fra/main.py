from src.service.in_fra.prefectures import prefectures, prefecture_dict
from src.service.in_fra.fetch_elements import fetch_elements
from src.service.in_fra.append_csv import append_csv, CSV_PATH
from src.lib.csv.create_csv_only_header import create_csv_only_header


PAGE_LIMIT = 217

create_csv_only_header(output_path=CSV_PATH)

print("fetching...")

for prefecture in prefectures:
    print(f"prefecture: {prefecture},{prefecture_dict[prefecture]}")

    for page in range(1, PAGE_LIMIT):
        print(f"\tpage {page}:")

        elements = fetch_elements(prefecture=prefecture, page=page)
        if not elements:
            break

        for element in elements:
            result = append_csv(element=element)
            if not result:
                break

        print("")

print("fetch done")
