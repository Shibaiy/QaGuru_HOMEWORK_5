
import shutil
import pytest
from selene import  browser, query
import wget
import os.path
from zipfile import ZipFile







@pytest.fixture(scope='module',autouse=True)
def download_and_archive_files():


    browser.open('https://github.com/Shibaiy/QaGuru_vvodnoe/blob/main/CSV.csv')
    download_URL = browser.element("//*[@data-testid='raw-button']").get(query.attribute("href"))
    wget.download(download_URL,'C:/Users/pc/PycharmProjects/QaGuru_HOMEWORK_5/tmp')
    browser.open('https://github.com/Shibaiy/QaGuru_vvodnoe/blob/main/XLSX.xlsx')
    download_URL = browser.element("//*[@data-testid='raw-button']").get(query.attribute("href"))
    wget.download(download_URL, 'C:/Users/pc/PycharmProjects/QaGuru_HOMEWORK_5/tmp')


    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = os.path.join(CURRENT_DIR, "resources")
    ARCHIVE_FILE = os.path.join(RESOURCE_DIR,'archive.zip')

    if not os.path.exists("resources"):
        os.mkdir("resources")

    with ZipFile(f'{ARCHIVE_FILE} ', 'w') as myzip:
        myzip.write('tmp/Demo.pdf',arcname='Demo.pdf')
        myzip.write('tmp/CSV.csv',arcname='CSV.csv')
        myzip.write('tmp/XLSX.xlsx', arcname='XLSX.xlsx')



    yield
    os.remove('C:/Users/pc/PycharmProjects/QaGuru_HOMEWORK_5/tmp/CSV.csv')
    os.remove('C:/Users/pc/PycharmProjects/QaGuru_HOMEWORK_5/tmp/XLSX.xlsx')
    shutil.rmtree(RESOURCE_DIR)










