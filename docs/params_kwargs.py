from typing import Optional
class kwargs:
    def __init__(self
                 ,email: str = None
                 ,pswd: str = None
                 ,manager: str = None
                 ,name: str = None
                 ,sellist1 : str = None
                 ,text : str = None) -> None:
        self.name = name
        self.pswd = pswd
        self.email = email
        pass
if __name__ == "__main__":
    user = {
        "pswd": "Password123!"
        ,"email": "chulsoo.kim@example.com"
        ,"name": "김철수"
    }
    #kwargs(**) 딕셔너리를 통째로 넘겨줄때 사용 / user 딕셔너리 통째로 넘겨주는거임
    #**의 특징 - 딕셔너리여야지만 가능, 딕셔너리를 function에 통째로 넘겨줌
    #kwargs(email=user["email"], name=user["name"])
    
    # kwargs(**user)
    kwargs(user)
    pass