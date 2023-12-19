def delete_line_from_file(file_path, line_to_delete):
    try:
        with open(file_path, 'r', encoding= 'UTF-8') as file:
            lines = file.readlines()
            lines = [line for line in lines if line.strip() != line_to_delete.strip()]
        with open(file_path, 'w', encoding= 'UTF-8') as file:
            file.writelines(lines)
            print(f"Рядок '{line_to_delete}' був успішно видалений з файлу.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {str(e)}")


file_path = 'file_path.txt'
line_to_delete = 'привіт'
delete_line_from_file(file_path, line_to_delete)