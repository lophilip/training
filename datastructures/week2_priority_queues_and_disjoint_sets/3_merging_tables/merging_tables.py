# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        self.union_manually(src_parent, dst_parent)
        
        #update max_row_count
        #self.max_row_count=max(self.row_counts)
        return True

    def get_parent(self, table):
        # find parent and compress path
        path_compress=True
        
        
        if path_compress:
            if table!=self.parents[table]:
                self.parents[table]=self.get_parent(self.parents[table])
            return self.parents[table]
        else:            
            return self.parents[table]
    
    def find(self, table):
        i=table
        while i != self.parents[i]:
            i=self.parents[i]
        return i
    
    
    def union_manually(self,i,j):#i is dest, j is source
        i_id=self.find(i) #root source of table
        j_id=self.find(j)
        
        returnvalue=False
        use_rank_huristics=True
        
        if i_id==j_id:
            returnvalue=False
        elif use_rank_huristics:
            if self.ranks[i_id] > self.ranks[j_id]:
                self.parents[j_id]=i_id
                self.row_counts[i_id]+=self.row_counts[j_id]
                self.row_counts[j_id]=0
                returnvalue=True
                
                if self.row_counts[i_id] > self.max_row_count:
                    self.max_row_count=self.row_counts[i_id]
            else:
                self.parents[i_id]=j_id
                self.row_counts[j_id]+=self.row_counts[i_id]
                self.row_counts[i_id]=0
                if self.ranks[i_id]==self.ranks[j_id]:
                    self.ranks[j_id]=self.ranks[i_id]+1
                returnvalue=True
                
                if self.row_counts[j_id] > self.max_row_count:
                    self.max_row_count=self.row_counts[j_id]
        else: #just use straight union, with no rank huristics
            self.parents[j_id]=i_id
            self.row_counts[i_id]+=self.row_counts[j_id]
            self.row_counts[j_id]=0
            
            if self.row_counts[i_id] > self.max_row_count:
                self.max_row_count=self.row_counts[i_id]
            returnvalue=True
            
        return returnvalue
            
                
        
        


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
