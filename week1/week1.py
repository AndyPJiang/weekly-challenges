from abc import ABC, abstractmethod
from typing import TypeVar, Generic,Sequence

T = TypeVar('T')

class BidirectionalIterator(Generic[T]):
    def __init__(self,iterator):
        self.iterator = iterator
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self) -> T:
        try:
            self.index+=1
            return self.iterator[self.index]
        except IndexError:
            self.index -=1
            raise StopIteration
    
    def __prev__(self) -> T:
        self.index-=1
        if self.index<0:
            self.index = 0
            raise StopIteration
        return self.iterator[self.index]
    
    def __hasNext__(self) -> bool:
        try:
            _ = self.__next__()
            self.index-=1
            return True
        except StopIteration:
            return False
    
    def __hasPrev__(self) -> bool:
        try:
            _ = self.__prev__()
            _ = self.__next__()
            return True
        except StopIteration:
            return False

class AbstractFlattenedBidirectionalIterator(ABC):
    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __next__(self):
        pass
    @abstractmethod
    def __prev__(self):
        pass


class FlattenedBidirectionalIterator(AbstractFlattenedBidirectionalIterator,Generic[T]):
    def __init__(self, iterators: Sequence[BidirectionalIterator[T]] ):
        
        # only keep non-empty iterators, i.e. [[],[1,2,3]] -> [[1,2,3]]
        self.iterators = []
        for iterator in iterators:
            if iterator.__hasNext__():
                self.iterators.append(iterator)

        self.i = -1

        # keeps track of if each iterator has finished
        self.counts = [0] * len(iterators)
 
    def __iter__(self):
        return self

    def __next__(self) -> T:
        n = len(self.iterators)
        count = 0
        while count < n:
            # index in a loop 0->1...n-1->0->1..
            self.i = (self.i + 1) % n
            cur = self.iterators[self.i]
            try:
                 return cur.__next__()
            except StopIteration:
                count+=1
                self.counts[self.i] += 1

        raise StopIteration


    def __prev__(self) -> T:
        n = len(self.iterators)
        count = 0
        cur = self.iterators[self.i]
        if cur.__hasPrev__():
            _ = cur.__prev__()

        # if at at the very beginning of the iterator 
        elif self.i==0:
            raise StopIteration
   
        while count < n:
            # index in a loop n-1->n-2...0->n-1->n-2...
            self.i = (self.i + n - 1) % n  
            cur = self.iterators[self.i]
            if self.counts[self.i] > 0:
                self.counts[self.i] -=1
                count+=1
            else:
                try:
                    current = cur.iterator[cur.index]
                    return current
                except:
                    count+=1

        raise StopIteration



iter1 = BidirectionalIterator([1,2,3])
iter2 = BidirectionalIterator([4,5])
iter3 = BidirectionalIterator([6,7,8])


inst = FlattenedBidirectionalIterator([iter1,iter2,iter3])

