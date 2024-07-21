import requests

# Функция для получения списка курсов из ProjectB
def get_courses_from_projectB():
    response = requests.get('http://localhost:8001/api/courses/')  # URL API ProjectB
    if response.status_code == 200:
        return response.json()  # Возвращаем данные в формате JSON
    return None
