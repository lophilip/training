from merging_tables import *



def developer_run_database():
    count=[1,1,1,1,1]
    merge=[(3,5),(2,4),(1,4),(5,4),(5,3)]
    db = Database(count)
    
    print (db)

    for i in range(len(merge)):
        dst, src = merge[i]
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)    
    
if __name__=='__main__':
    developer_run_database()
    