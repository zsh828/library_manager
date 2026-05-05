import pytest
from src.library import LibraryManager, Book


class TestLibraryManager:
    """测试图书管理器类"""
    
    def setup_method(self):
        """每个测试方法执行前初始化"""
        self.manager = LibraryManager()
    
    def test_add_book_success(self):
        """测试成功添加图书"""
        result = self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        assert result is True
        assert self.manager.get_book_count() == 1
    
    def test_add_book_duplicate_isbn(self):
        """测试添加重复ISBN的图书"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        result = self.manager.add_book("Python进阶", "李四", "978-7-111-12345-6")
        assert result is False
        assert self.manager.get_book_count() == 1
    
    def test_add_multiple_books(self):
        """测试添加多本图书"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        self.manager.add_book("Java编程", "李四", "978-7-111-12345-7")
        self.manager.add_book("C++编程", "王五", "978-7-111-12345-8")
        
        assert self.manager.get_book_count() == 3
    
    def test_get_book_by_isbn_found(self):
        """测试根据ISBN查询到图书"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        book = self.manager.get_book_by_isbn("978-7-111-12345-6")
        
        assert book is not None
        assert book.title == "Python编程"
        assert book.author == "张三"
        assert book.isbn == "978-7-111-12345-6"
    
    def test_get_book_by_isbn_not_found(self):
        """测试根据ISBN查询不到图书"""
        book = self.manager.get_book_by_isbn("978-7-111-99999-9")
        assert book is None
    
    def test_search_by_title_exact_match(self):
        """测试精确匹配书名查询"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        self.manager.add_book("Java编程", "李四", "978-7-111-12345-7")
        
        results = self.manager.search_by_title("Python编程")
        assert len(results) == 1
        assert results[0].title == "Python编程"
    
    def test_search_by_title_partial_match(self):
        """测试部分匹配书名查询"""
        self.manager.add_book("Python编程入门", "张三", "978-7-111-12345-6")
        self.manager.add_book("Python高级教程", "李四", "978-7-111-12345-7")
        self.manager.add_book("Java编程", "王五", "978-7-111-12345-8")
        
        results = self.manager.search_by_title("Python")
        assert len(results) == 2
        
        titles = [book.title for book in results]
        assert "Python编程入门" in titles
        assert "Python高级教程" in titles
    
    def test_search_by_title_case_insensitive(self):
        """测试书名查询不区分大小写"""
        self.manager.add_book("PYTHON编程", "张三", "978-7-111-12345-6")
        
        results = self.manager.search_by_title("python")
        assert len(results) == 1
        assert results[0].title == "PYTHON编程"
    
    def test_search_by_title_no_match(self):
        """测试书名查询无匹配结果"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        
        results = self.manager.search_by_title("JavaScript")
        assert len(results) == 0
    
    def test_delete_book_success(self):
        """测试成功删除图书"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        result = self.manager.delete_book("978-7-111-12345-6")
        
        assert result is True
        assert self.manager.get_book_count() == 0
        assert self.manager.get_book_by_isbn("978-7-111-12345-6") is None
    
    def test_delete_book_not_found(self):
        """测试删除不存在的图书"""
        result = self.manager.delete_book("978-7-111-99999-9")
        assert result is False
        assert self.manager.get_book_count() == 0
    
    def test_list_all_books_empty(self):
        """测试空图书馆列出所有图书"""
        books = self.manager.list_all_books()
        assert len(books) == 0
        assert isinstance(books, list)
    
    def test_list_all_books_with_data(self):
        """测试有数据时列出所有图书"""
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        self.manager.add_book("Java编程", "李四", "978-7-111-12345-7")
        
        books = self.manager.list_all_books()
        assert len(books) == 2
        
        titles = [book.title for book in books]
        assert "Python编程" in titles
        assert "Java编程" in titles
    
    def test_book_to_dict(self):
        """测试图书对象转字典"""
        book = Book("Python编程", "张三", "978-7-111-12345-6")
        book_dict = book.to_dict()
        
        assert book_dict["title"] == "Python编程"
        assert book_dict["author"] == "张三"
        assert book_dict["isbn"] == "978-7-111-12345-6"
    
    def test_book_equality(self):
        """测试图书对象相等性比较"""
        book1 = Book("Python编程", "张三", "978-7-111-12345-6")
        book2 = Book("Python编程", "张三", "978-7-111-12345-6")
        book3 = Book("Java编程", "李四", "978-7-111-12345-7")
        
        assert book1 == book2
        assert book1 != book3
    
    def test_get_book_count(self):
        """测试获取图书总数"""
        assert self.manager.get_book_count() == 0
        
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        assert self.manager.get_book_count() == 1
        
        self.manager.add_book("Java编程", "李四", "978-7-111-12345-7")
        assert self.manager.get_book_count() == 2
        
        self.manager.delete_book("978-7-111-12345-6")
        assert self.manager.get_book_count() == 1
    
    def test_complex_workflow(self):
        """测试复杂工作流"""
        # 添加图书
        self.manager.add_book("Python编程", "张三", "978-7-111-12345-6")
        self.manager.add_book("Java编程", "李四", "978-7-111-12345-7")
        self.manager.add_book("Go语言编程", "王五", "978-7-111-12345-8")
        
        # 查询所有图书
        all_books = self.manager.list_all_books()
        assert len(all_books) == 3
        
        # 按书名搜索
        python_books = self.manager.search_by_title("Python")
        assert len(python_books) == 1
        
        # 按ISBN查询
        java_book = self.manager.get_book_by_isbn("978-7-111-12345-7")
        assert java_book is not None
        assert java_book.title == "Java编程"
        
        # 删除图书
        self.manager.delete_book("978-7-111-12345-8")
        assert self.manager.get_book_count() == 2
        
        # 再次查询所有图书
        remaining_books = self.manager.list_all_books()
        assert len(remaining_books) == 2
        remaining_titles = [book.title for book in remaining_books]
        assert "Go语言编程" not in remaining_titles