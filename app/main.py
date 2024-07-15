# FastAPI를 Import 받습니다.
from fastapi import FastAPI


# FastAPI 인스턴스를 생성합니다.
app = FastAPI()


# 서버 경로 http://127.0.0.1:8080 에 접근하면
# {"message": "Hello World"}를 반환하는 API를 선언합니다.
@app.get("/")
async def root():
    return {"message": "Hello World"}


# 서버 경로 http://127.0.0.1:8080/hello/{name} 에 접근하면
# {"message": f"Hello {name}"}을 반환하는 API를 선언합니다.
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
