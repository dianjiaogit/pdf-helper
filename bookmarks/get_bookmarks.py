from PyPDF2 import PdfFileReader
from utils import path_split
import os


def bookmark_dict(bookmark_list):
    '''return dict of bookmarks
    ref: https://stackoverflow.com/questions/54303318/read-all-bookmarks-from-a-pdf-document-and-create-a-dictionary-with-pagenumber-a
    '''
    result = {}
    for item in bookmark_list:
        if isinstance(item, list):
            result.update(bookmark_dict(item))
        else:
            result[reader.getDestinationPageNumber(item)] = item.title
    return result


def write_bookmark(bookmarks):
    content = ''
    for page, title in bookmarks.items():
        content += f"{title} @{page}\n"
    return content


if __name__ == '__main__':
    file_path = input('请输入文件路径：')

    reader = PdfFileReader(file_path)
    bookmarks = bookmark_dict(reader.getOutlines())

    _, file_name, _ = path_split(file_path)
    with open(os.path.join('bookmarks', file_name + '.txt'), 'w') as f:
        f.write(write_bookmark(bookmarks))
