create_MyTable = '''
CREATE TABLE MyTable(
    name TEXT,
    url TEXT,
    account_id TEXT NOT NULL,
    password TEXT NOT NULL,
    note TEXT,
    PRIMARY KEY(name,url)
)
'''

check_MyTable = '''
SELECT
    COUNT(*) 
FROM
    sqlite_master
WHERE
    TYPE='table' AND name= 'MyTable'
'''

add_MyTable = '''
INSERT INTO MyTable(
    name,
    url,
    account_id,
    password,
    note
) VALUES(
    ?,
    ?,
    ?,
    ?,
    ?
)
'''

get_MyTable = '''
SELECT 
    * 
FROM
    MyTable
WHERE
    name = ? OR url = ? 
'''

get_only_MyTable = '''
SELECT 
    * 
FROM
    MyTable
WHERE
    name = ? AND url = ? 
'''

get_all_MyTable = '''
SELECT 
    * 
FROM
    MyTable
'''

update_Mytable = '''
UPDATE 
    MyTable
SET
    name = ?,
    url = ?,
    account_id = ?,
    password = ?,
    note = ?
WHERE
    name = ?
AND url = ?
'''

delete_Mytable = '''
DELETE 
FROM
    MyTable
WHERE
    name = ?
AND url = ?
'''