from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "Это, так называемый, калькулятор."}

@app.get("/add/{num1}/{num2}")
def add_numbers(num1: int, num2: int):
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