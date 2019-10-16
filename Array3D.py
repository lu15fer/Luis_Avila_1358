#Array 3D

'''
get_num_rows()
get_num_cols()
get_num_depth()
set_otem(r,c,d,value)
get_item(r,c,d)
clearing(value)
to_string()
'''

class Array3D:

    def __init__(self,rows,cols,depth):
        self.__data=[]
        self.__rows=rows
        self.__cols=cols
        self.__depth=depth

        self.__data=[[[None for rows in range(self.__rows)] for cols in range(self.__cols)] for depth in range(self.__depth)]

    

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__rows
    
    def get_num_cols(self):
        return self.__cols

    def get_num_depth(depth):
        return self.__depth

    def set_item(self,rows,cols,depth,value):
        #if rows>=0 and cols>=0 and depth>=0 and rows<self.__rows and cols<self.__cols and depth<self.__depth
            self.__data[depth][cols][rows]=value

        
    def get_item(self,rows,cols,depth):
        return self.__data[depth][cols][rows]
    

    def clearing(self,value):
        for i in range(self.__depth):
            for j in range(self.__cols):
                for k in range(self.__rows):
                    self.__data[i][j][k]=value
                    

    

'''def main():
    
    A3=Array3D(3,3,2)
    A3.to_string()
    A3.clearing(1)
    A3.to_string()
    A3.set_item(1,2,0,33)
    A3.to_string()


main()
            
'''
