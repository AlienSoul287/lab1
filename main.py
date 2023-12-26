from fastapi import FastAPI# Импортирование библиотек

app = FastAPI() # Инициализация веб-приложения

@app.get("/")
def read_main():  #нач страницы, затем роуты (тоже явл роутом)
    return {"message": "Это, так называемый, калькулятор."}

@app.get("/add/{num1}/{num2}") # Путь для path-запроса
def add_numbers(num1: int, num2: int): # Создание функции, которая принимает в себя 2 числа с плавающей точкой в качестве аргументов
    return {"result": num1 + num2}

@app.get("/subtract/{num1}/{num2}")
def subtract_numbers(num1: int, num2: int):
    return {"result": num1 - num2}

@app.get("/multiply/{num1}/{num2}")
def multiply_numbers(num1: int, num2: int):
    return {"result": num1 * num2}

@app.get("/divide/{num1}/{num2}")
def divide_numbers(num1: float, num2: float):
    if num2 != 0:
        return {"result": num1 / num2}
    else:
        return {"error": "Деление на 0 невозможно!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
