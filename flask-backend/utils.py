post = {"mmr": "1000"}
# db.ian.insert_one(post)
# delete_many = db.ian.delete_many({})
names = ["ian", "liam", "will", "nicky", "steve", "vevey", "yuuki", "aaron", "erik", "cam"]
def add_user(name, db):
    #print(db.list_collection_names())
    if name not in db.list_collection_names():
        col = db[name]
        col.insert_one(post)

def add_collections(db):
    for i in names:
        col = db[i]
        col.insert_one(post)

def delete_documents_in_all(db):
    for i in names:
        col = db[i]
        col.delete_many({})

def find_docs(db):
    for i in db.ian.find():
        print(i)

def find_last_document(db, col):
    if db[col].count() > 0:
        sorted_list = db[col].find().sort("_id", -1).limit(1)

        return sorted_list


#add_collections(client.mmr)
#delete_documents_in_all(client.mmr)
