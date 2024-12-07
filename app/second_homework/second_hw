def get_cats_info(path):
    list_cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                id, name, age = line.split(",")
                list_cats.append({
                    "id":id,
                    "name": name,
                    "age": age[:1],
                })
    except FileNotFoundError as e:
        print(e)
    finally:
        return list_cats

cats_info = get_cats_info("second_homework/cat_data.txt")
print(cats_info)