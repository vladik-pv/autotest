import requests


base_url = "https://ru.yougile.com/api-v2"


# Авторизация
def test_auth():

    auth_data = {
        "login": "vladik_pv@mail.ru",
        "password": "545335Yyy!",
        "companyId": "05ede029-3256-4d0a-bed5-b0ccb756f302"
    }

# Получение ключа авторизации
    resp = requests.post(base_url + "/auth/keys", json=auth_data)
    assert resp.status_code == 201, "Ошибка при получении ключа авторизации"
    key = resp.json()["key"]
    return key


# Создание проекта
def test_create_project():

    key = test_auth()

# Данные для создания проекта
    project = {
        "title": "MyProject1"
    }

# Заголовки для запроса
    my_headers = {
        "Authorization": f"Bearer {key}"
    }

# Создание проекта
    resp = requests.post(
        f"{base_url}/projects", json=project, headers=my_headers
        )
    assert resp.status_code == 201, "Ошибка при создании проекта"
    new_id = resp.json()["id"]
    return new_id


# Данные для авторизации с неверным паролем
def test_create_project_error():

    auth_data = {
        "login": "vladik_pv@mail.ru",
        "password": "wrong_password",
        "companyId": "05ede029-3256-4d0a-bed5-b8ccb756fa82"
    }
# Получение ключа авторизации
    resp = requests.post(f"{base_url}/auth/keys", json=auth_data)
    assert resp.status_code != 201, "Ключ получен с неверными данными"

# Данные для создания проекта
    project = {
        "title": "MyProject1"
    }

# Заголовки для запроса (ключ не будет получен из-за ошибки авторизации)
    my_headers = {
        "Authorization": "Bearer invalid_key"
    }

# Попытка создания проекта
    resp = requests.post(
        f"{base_url}/projects", json=project, headers=my_headers
        )
    assert resp.status_code != 201, "Проект создан с неверными данными"


# Получение по ID
def test_get_by_id():
    new_id = test_create_project()
    key = test_auth()
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    resp = requests.get(f"{base_url}/projects/{new_id}", headers=my_headers)
    assert resp.status_code == 200, "Ошибка при получении проекта по ID"
    assert resp.json()["id"] == new_id, "Получен неверный ID проекта"


# Негативная проверка с несуществующим id
def test_get_by_id_negative():
    key = test_create_project()
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    non_existent_id = "00000000-0000-0000-0000-000000000000"

    resp = requests.get(
        f"{base_url}/projects/{non_existent_id}", headers=my_headers
        )
    assert resp.status_code == 404, "Ожидалась ошибка 404"


# Изменения
def test_put():
    new_id = test_create_project()
    key = test_auth()
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    project = {
        "deleted": False,
        "title": "SkyPro"
    }
    resp = requests.put(
        f"{base_url}/projects/{new_id}", json=project, headers=my_headers
    )
    assert resp.status_code == 200, "Ошибка при изменении проекта"
    assert resp.json()["id"] == new_id, "Получен неверный ID проекта"

# Выполняем GET-запрос для получения данных проекта
    get_resp = requests.get(
        f"{base_url}/projects/{new_id}", headers=my_headers
        )

# Проверяем, что статус код GET-запроса 200
    assert get_resp.status_code == 200, "Ошибка при получении данных проекта"

# Проверяем, что title в ответе соответствует ожидаемому значению
    assert get_resp.json()[
        "title"
        ] == "SkyPro", "Title несоответствует ожидаемому значению"


# Негативная проверка с несуществующим id
def test_put_negative():

    key = test_create_project()
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    project = {
        "deleted": False,
        "title": "MyProject1"
    }
    resp = requests.put(
        f"{base_url}/projects/{non_existent_id}",
        json=project, headers=my_headers
        )
    assert resp.status_code == 404, "Ожидалась ошибка 404"
