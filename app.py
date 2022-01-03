# from model import Word
from random import randint

from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
from uvicorn import run

from databases import Database


# engine = create_engine(
#     f"sqlite:///words.db",
#     connect_args={"check_same_thread": False},
#     echo=False,
# )
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db():
    # db = SessionLocal()
    await database.connect()
    try:
        yield database
    except:  # noqa
        # database.rollback()
        pass
    finally:
        await database.disconnect()
        # db.close()


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
    # print(0)
    # try:
    #     database = Database("sqlite:///words.db")
    # except Exception as e:
    #     print(e)

    # print(1)
    # await database.connect()
    # print(2)
    sql = "SELECT word FROM word WHERE id = :id"

    # print("in get_words_lst")
    # print("x =", x)
    words_lst = []
    words_counter = 0
    while True:
        temp_pk = randint(2, 65000)
        try:
            # word = db.query(Word).get(temp_pk).word
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

    # await database.disconnect()
    return words_lst


# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.url_map.strict_slashes = False
# db.init_app(app)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/words/<int:x>')
# def get_words_lst(x: int):
#     words_lst = []
#     words_counter = 0
#     while True:
#         temp_pk = randint(2, 65000)
#         try:
#             word = Word.query.get(temp_pk).word
#             if word in words_lst:
#                 continue
#             words_lst.append(word)
#             words_counter += 1
#         except Exception as e:
#             print(e)
#         finally:
#             if words_counter >= x:
#                 break
#
#     return jsonify(words_lst)
#
#
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'Word': Word}


if __name__ == '__main__':
    # app.run()
    run(
        "app:app",
        host='localhost',
        port=8000,
        reload=True
    )

