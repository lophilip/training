# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class query_direct: #direct addressing
    def __init__(self):
        self.phone_book=[]
        self.init_phone_book()
    def init_phone_book(self,max_number=pow(10,7)):
        """initialize phone book with max_number of None values"""
        self.phone_book=[None]*max_number
    def add(self,number,name):
        self.phone_book[number]=name
    def del_num(self,number):
        self.phone_book[number]=None
    def find(self,number):
        if number <= len(self.phone_book):
            return self.phone_book[number]
        else:
            return None

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def process_queries_direct(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = query_direct()
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts.add(cur_query.number,cur_query.name)
        elif cur_query.type == 'del':
            contacts.del_num(cur_query.number)
        elif cur_query.type == 'find':
            response = contacts.find(cur_query.number)
            if response is None:
                response = 'not found'
            result.append(response)
        else:
            print('unknown query type')
            assert(True), "unknown query type"
    return result
if __name__ == '__main__':
    #write_responses(process_queries(read_queries()))
    write_responses(process_queries_direct(read_queries()))

