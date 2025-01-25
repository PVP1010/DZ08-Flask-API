from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    quote = get_random_quote()  # Получение случайной цитаты
    return render_template('index.html', quote=quote)  # Передача данных в шаблон

def get_random_quote():
    """
    Запрашивает случайную цитату с публичного API.
    """
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        data = response.json()  # Получаем JSON-ответ
        print("Ответ от API:", data)  # Отладочный вывод
        return {
            "content": data.get("content", "Цитата недоступна"),
            "author": data.get("author", "Неизвестный автор")
        }
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе API: {e}")
        return {
            "content": "Не удалось загрузить цитату. Попробуйте позже.",
            "author": ""
        }

if __name__ == '__main__':
    app.run(debug=True)

