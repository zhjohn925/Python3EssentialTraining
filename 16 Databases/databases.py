#!/usr/bin/python3

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test(t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test(t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test(t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test(t1, i1) values (?, ?)', ('four', 4))
    db.execute('insert into test(t1, i1) values (?, ?)', ('five', 5))
    db.execute('insert into test(t1, i1) values (?, ?)', ('six', 6))
    # run commit() after database is changed
    db.commit()
    cursor = db.execute('slect * from test oder by t1')
    for row in cursor :
        print (row)
        

def main2():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlites.Row
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test(t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test(t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test(t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test(t1, i1) values (?, ?)', ('four', 4))
    db.execute('insert into test(t1, i1) values (?, ?)', ('five', 5))
    db.execute('insert into test(t1, i1) values (?, ?)', ('six', 6))
    # run commit() after database is changed
    db.commit()
    cursor = db.execute('slect * from test oder by t1')
    for row in cursor :
        print (row)       #row is iterate object
        print(dict(row))
        print(row['t1'], row['i1'])

if __name__ == "__main__": main()
