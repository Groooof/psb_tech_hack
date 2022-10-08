import sqlalchemy as sa
import sqlalchemy.ext.asyncio as as_sa


async def test_select(con: as_sa.AsyncConnection):
    query = '''
    SELECT * FROM users;
    '''
    res = await con.execute(sa.text(query))
    return res.fetchall()
