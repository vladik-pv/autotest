from sqlalchemy import create_engine, text, inspect


connecting = "postgresql://vladik_pv:123321@localhost:5432/QA"


def test_db_connection():
    engine = create_engine(connecting)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert tables[7] == 'places'


def test_create_place():
    engine = create_engine(connecting)
    create = text(
        'insert into places\
            ("place_id", "place_name") values (:place_id, :place_name)'
        )
    with engine.connect() as connection:
        connection.execute(create.bindparams(place_id=6, place_name='озеро'))
        connection.commit()
    delete = text("delete from places where place_id = :place_id")
    with engine.connect() as connection:
        connection.execute(delete, {"place_id": 6})
        connection.commit()


def test_update_place():
    engine = create_engine(connecting)
    create = text(
        'insert into places\
            ("place_id", "place_name") values (:place_id, :place_name)'
        )
    with engine.connect() as connection:
        connection.execute(create.bindparams(place_id=6, place_name='озеро'))
        connection.commit()
    updata = text(
        'update places set place_size\
             = :place_size where place_id = :place_id'
        )
    with engine.connect() as connection:
        connection.execute(updata, {"place_size": "50", "place_id": 6})
        connection.commit()
    delete = text("delete from places where place_id = :place_id")
    with engine.connect() as connection:
        connection.execute(delete, {"place_id": 6})
        connection.commit()


def test_delete_place():
    engine = create_engine(connecting)
    create = text(
        'insert into places\
            ("place_id", "place_name") values (:place_id, :place_name)'
        )
    with engine.connect() as connection:
        connection.execute(create.bindparams(place_id=6, place_name='озеро'))
        connection.commit()
    delete = text("delete from places where place_id = :place_id")
    with engine.connect() as connection:
        connection.execute(delete, {"place_id": 6})
        connection.commit()
