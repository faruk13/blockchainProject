pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract NewBook {

    struct ChapterData {
        // string chapterID;
        string title;
        uint pages;
    }

    struct BookData {
        // string bookID;
        ChapterData[] chapters;
    }

    mapping(uint => BookData) books; // bookId => BookData

    function addChapter(uint _bookID, string memory title, uint pages) public {
        ChapterData memory c = ChapterData({
            title: title,
            pages: pages
        });
        books[_bookID].chapters.push(c);
    }
    function getChapterByBook(uint _bookID) public view returns(
    ChapterData[] memory chapters
    ){
        return books[_bookID].chapters;
    }
}