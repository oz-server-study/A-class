# FastAPI를 Import 받습니다.
from fastapi import FastAPI


# FastAPI 인스턴스를 생성합니다.
app = FastAPI()
people = [
    {"name": "김대정", "role": "leader", "class": ["A", "B"]},
    {"name": "강승진", "role": "member", "class": ["A"]},
    {"name": "송미현", "role": "member", "class": ["A"]},
    {"name": "최원경", "role": "member", "class": ["A"]},
    {"name": "김태우", "role": "member", "class": ["B"]},
    {"name": "정민준", "role": "member", "class": ["B"]},
    {"name": "안우진", "role": "member", "class": ["A"]},
]


# 서버 경로 http://127.0.0.1:8000 에 접근하면
# {"message": "Hello World"}를 반환하는 API를 선언합니다.
@app.get("/")
async def root():
    return {"message": "Hello World"}


# 서버 경로 http://127.0.0.1:8000/hello/{name} 에 접근하면
# {"message": f"Hello {name}"}을 반환하는 API를 선언합니다.
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 서버 경로 http://127.0.0.1:8000/person/{name} 에 접근하면
# 검색한 사용자를 반환하는 API를 선언합니다.
# 검색한 사용자가 없다면, message를 반환합니다.
@app.get("/person/{name}")
async def get_person(name: str):
    for person in people:
        if person['name'] == name:
            return dict(person=person)

    return {"message": f"No person named {name}"}


# 서버 경로 http://127.0.0.1:8000/people 에 접근하면
# 저장된 모든 사용자의 정보가 반환됩니다.
@app.get("/people")
async def get_people():
    return dict(people=people)

