"""
图书管理模块
提供图书的增删查改功能
"""

from typing import List, Dict, Optional


class Book:
    """图书类，表示一本图书的基本信息"""
    
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def to_dict(self) -> Dict[str, str]:
        """将图书对象转换为字典"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"


class LibraryManager:
    """图书管理器类，管理所有图书"""
    
    def __init__(self):
        # 使用字典存储图书，key为ISBN，value为Book对象
        self._books: Dict[str, Book] = {}
    
    def add_book(self, title: str, author: str, isbn: str) -> bool:
        """
        添加图书
        
        Args:
            title: 书名
            author: 作者
            isbn: ISBN号
            
        Returns:
            bool: 添加成功返回True，如果ISBN已存在返回False
        """
        if isbn in self._books:
            return False
        
        book = Book(title=title, author=author, isbn=isbn)
        self._books[isbn] = book
        return True
    
    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        根据ISBN查询图书
        
        Args:
            isbn: ISBN号
            
        Returns:
            Book或None: 找到图书返回Book对象，否则返回None
        """
        return self._books.get(isbn)
    
    def search_by_title(self, title: str) -> List[Book]:
        """
        按书名模糊查询图书
        
        Args:
            title: 书名关键词
            
        Returns:
            List[Book]: 匹配的图书列表
        """
        results = []
        for book in self._books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results
    
    def delete_book(self, isbn: str) -> bool:
        """
        删除图书
        
        Args:
            isbn: ISBN号
            
        Returns:
            bool: 删除成功返回True，如果ISBN不存在返回False
        """
        if isbn not in self._books:
            return False
        
        del self._books[isbn]
        return True
    
    def list_all_books(self) -> List[Book]:
        """
        列出所有图书
        
        Returns:
            List[Book]: 所有图书的列表
        """
        return list(self._books.values())
    
    def get_book_count(self) -> int:
        """获取图书总数"""
        return len(self._books)