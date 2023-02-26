# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

class hash_chain_class():
    def __init__(self,num_buckets):
        assert isinstance(num_buckets,int),'buckets should be int, and number of buckts'
        self.buckets=[]
        self.chain=[]
        self.num_buckets=num_buckets
        for i in range (0,num_buckets):
            self.buckets.append(i)
            self.chain.append([])
    
    def calculate_hash(self,thestring) -> int:
        ans=0
        multiplier = 263
        prime = 1000000007
        assert isinstance(thestring,str),'thestring should be a string, of which hash will be returned'

        for c in reversed(thestring):
            ans = (ans * multiplier + ord(c)) % prime
        ans=ans%self.num_buckets

        return ans
    
    def add_string(self,input) -> None:
        hash=self.calculate_hash(input)
        added=False
        
        stringlist=[]
        if hash<self.num_buckets:
            stringlist=self.chain[hash]
        else:
            stringlist=self.chain[self.num_buckets-1]
            
        if input not in stringlist:
            stringlist.append(input)
            added=True
            
        return added

    def del_string(self,input) -> bool:
        returnvalue=False

        hash=self.calculate_hash(input)
        list_string=[]
        index=-1
        if hash<self.num_buckets:
            list_string=self.chain[hash]
            index=hash
        else:
            list_string=self.chain[self.num_buckets-1]
            index=self.num_buckets-1

        list_string.reverse()

        try:
            string_index=list_string.index(input)
        except ValueError:
            string_index=-1

        if string_index!=-1:
            list_string.pop(string_index)
            returnvalue=True
            
        list_string.reverse()

        return returnvalue

    def find_string(self,input) -> bool:
        found=False

        hash=self.calculate_hash(input)
        index=-1
        if hash<self.num_buckets:
            index=hash
        else:
            index=self.num_buckets-1
        
        list_string=self.chain[index]

        if input in list_string:
            found=True

        return found
    
    def check (self, index) -> list:
        list_string=[]
        if index<self.num_buckets:
            list_string=list(self.chain[index])
        else:
            list_string=list(self.chain[self.num_buckets-1])

        list_string.reverse()
        return list_string

class QueryProcessor_hash_chains:

    def __init__(self, bucket_count):
        self.hash_chain=hash_chain_class(bucket_count)

    def read_query(self):
        return Query(input().split())
 
    def process_query(self, query):
        if query.type == "check":

            list_string=self.hash_chain.check(query.ind)

            printout=''
            for x in list_string:
                printout+=x
                printout+=' '
            printout=printout[:-1]
            print(printout)

            
        elif query.type == 'find':
            found=self.hash_chain.find_string(query.s)
            if found:
                print('yes')
            else:
                print('no')
        elif query.type == 'add':
            self.hash_chain.add_string(query.s)
        elif query.type == 'del':
            self.hash_chain.del_string(query.s)
        else:
            print('error unknown query type %s'%query.type)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())



if __name__ == '__main__':
    bucket_count = int(input())
    #proc = QueryProcessor(bucket_count)
    proc = QueryProcessor_hash_chains(bucket_count)
    proc.process_queries()
