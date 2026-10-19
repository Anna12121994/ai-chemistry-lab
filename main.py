import csv

from chemistry_model import predict_solubility
from molecules import molecules


RESULT_FILE = "chemistry_results.csv"


def analyze_molecules():
    results = []

    print()
    print("АНАЛІЗ РЕЧОВИН ")
    print()

    for molecule in molecules:
        name = molecule["name"]
        formula = molecule["formula"]
        smiles = molecule["smiles"]

        try:
            predicted_value = predict_solubility(smiles)

            result = {
                "molecule_name": name,
                "formula": formula,
                "smiles": smiles,
                "predicted_property": "water_solubility",
                "predicted_value": predicted_value
            }

            results.append(result)

            print(
                name,
                "-",
                round(predicted_value, 4),
                "log mol/L"
            )

        except Exception as error:
            print("Помилка для", name, ":", error)

    return results


def save_to_csv(results):
    with open(
        RESULT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        fieldnames = [
            "molecule_name",
            "formula",
            "smiles",
            "predicted_property",
            "predicted_value"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    print()
    print("Результати збережено у:", RESULT_FILE)


def show_results(results):
    print()
    print("РЕЗУЛЬТАТИ")

    if not results:
        print("Результатів поки немає.")
        return

    for result in results:
        print()
        print("Речовина:", result["molecule_name"])
        print("Формула:", result["formula"])
        print("SMILES:", result["smiles"])
        print(
            "Розчинність:",
            round(result["predicted_value"], 4),
            "log mol/L"
        )


def sort_results(results):
    if not results:
        print("Спочатку виконайте аналіз.")
        return

    sorted_results = sorted(
        results,
        key=lambda x: x["predicted_value"],
        reverse=True
    )

    print()
    print("СОРТУВАННЯ ")

    for result in sorted_results:
        print(
            result["molecule_name"],
            "-",
            round(result["predicted_value"], 4),
            "log mol/L"
        )


def search_molecule(results):
    if not results:
        print("Спочатку виконайте аналіз.")
        return

    name = input("Введіть назву речовини: ").lower()

    found = False

    for result in results:
        if name in result["molecule_name"].lower():
            print()
            print("Речовина знайдена:")
            print("Назва:", result["molecule_name"])
            print("Формула:", result["formula"])
            print("SMILES:", result["smiles"])
            print(
                "Розчинність:",
                round(result["predicted_value"], 4),
                "log mol/L"
            )

            found = True

    if not found:
        print("Речовину не знайдено.")


def compare_molecules(results):
    if not results:
        print("Спочатку виконайте аналіз.")
        return

    first_name = input("Перша речовина: ").lower()
    second_name = input("Друга речовина: ").lower()

    first = None
    second = None

    for result in results:
        if first_name in result["molecule_name"].lower():
            first = result

        if second_name in result["molecule_name"].lower():
            second = result

    if first is None or second is None:
        print("Одну або обидві речовини не знайдено.")
        return

    print()
    print(" ПОРІВНЯННЯ")

    print(
        first["molecule_name"],
        ":",
        round(first["predicted_value"], 4)
    )

    print(
        second["molecule_name"],
        ":",
        round(second["predicted_value"], 4)
    )

    if first["predicted_value"] > second["predicted_value"]:
        print(first["molecule_name"], "має вищу прогнозовану розчинність.")

    elif second["predicted_value"] > first["predicted_value"]:
        print(second["molecule_name"], "має вищу прогнозовану розчинність.")

    else:
        print("Прогнозовані значення однакові.")


def main():
    results = []

    while True:
        print()

        print("    AI CHEMISTRY LAB")

        print("1. Проаналізувати 10 речовин")
        print("2. Показати результати")
        print("3. Сортувати за розчинністю")
        print("4. Пошук речовини")
        print("5. Порівняти дві речовини")
        print("0. Вихід")

        choice = input("Оберіть пункт: ")

        if choice == "1":
            results = analyze_molecules()
            save_to_csv(results)

        elif choice == "2":
            show_results(results)

        elif choice == "3":
            sort_results(results)

        elif choice == "4":
            search_molecule(results)

        elif choice == "5":
            compare_molecules(results)

        elif choice == "0":
            print("Програму завершено.")
            break

        else:
            print("Невірний пункт меню.")


main()