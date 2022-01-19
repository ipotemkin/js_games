from random import randint, seed

from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import run

from databases import Database


async def get_db():
    await database.connect()
    try:
        yield database
    except Exception as e:
        print(e)
        # database.rollback()
        await database.transaction().rollback()
    finally:
        await database.disconnect()


app = FastAPI(title='Games on FastAPI',
              description='This is a learning project on JS and Fast API',
              version='1.0.0')

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')

try:
    database = Database("sqlite:///words.db")
except Exception as e:
    print(e)
    exit(2)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/words/{x}')
async def get_words_lst(x: int, db: Database = Depends(get_db)):
    seed(randint(0, 1000))
    sql = "SELECT word FROM word WHERE id = :id"
    words_lst = []
    words_counter = 0
    while True:
        temp_pk = randint(2, 65000)
        try:
            res = await db.fetch_one(query=sql, values={"id": temp_pk})
            word = res[0]
            if word in words_lst:
                continue
            words_lst.append(word)
            words_counter += 1
        except Exception as e:
            print(e)
        finally:
            if words_counter >= x:
                break
    return words_lst


if __name__ == '__main__':
    run(
        "app:app",
        host='localhost',
        port=8000,
        reload=True
    )
