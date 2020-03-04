from django.test import TestCase
from app.models import User
from django.urls import reverse


class AppImportDataTest(TestCase):

    def generate_test_file1(self):
        file_test1 = open('test1.csv', 'w', encoding="utf-8")
        file_test1.write('name,surname,birth_date,position\n')
        file_test1.write('Святополк,Одинцова,1919-09-12,Communist')
        file_test1.close()
        return file_test1

    def generate_test_file2(self):
        file_test2 = open('test2.txt', 'w', encoding="utf-8")
        file_test2.write('name,surname,birth_date,position\n')
        file_test2.write('Святополк,Одинцова,1919-09-12,Communist')
        file_test2.close()
        return file_test2

    def generate_test_file3(self):
        file_test3 = open('test3.csv', 'w')
        file_test3.close()
        return file_test3

    def generate_test_file4(self):
        file_test4 = open('test4.csv', 'w', encoding="utf-8")
        file_test4.write('surname,birth_date,position\n')
        file_test4.write('Одинцова,1919-09-12,Communist')
        file_test4.close()
        return file_test4

    def generate_test_file5(self):
        file_test5 = open('test5.csv', 'w', encoding="utf-8")
        file_test5.write('surname,birth_date,position,name\n')
        file_test5.write('Одинцова,1919-09-12,Communist,Святополк')
        file_test5.close()
        return file_test5

    def generate_test_file6(self):
        file_test6 = open('test6.csv', 'w', encoding="utf-8")
        file_test6.write('name,surname,birth_date,position\n')
        file_test6.write('Святополк,Одинцова,191912,Communist')
        file_test6.close()
        return file_test6

    def generate_test_file7(self):
        file_test7 = open('test7.csv', 'w', encoding="utf-8")
        file_test7.write('name,surname,birth_date,position\n')
        file_test7.write('Святополкaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,Одинцова,1919-09-12,Communist')
        file_test7.close()
        return file_test7

    def generate_test_file8(self):
        file_test8 = open('test8.csv', 'w', encoding="utf-8")
        file_test8.write('name,surname,birth_date,position\n')
        file_test8.write(
            'Святополк, Одинцовааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа,1919-09-12,Communist')
        file_test8.close()
        return file_test8

    def generate_test_file9(self):
        file_test9 = open('test9.csv', 'w', encoding="utf-8")
        file_test9.write('name,surname,birth_date,position\n')
        file_test9.write(
            'Святополк,Одинцова,1919-09-12,Communisttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')
        file_test9.close()
        return file_test9

    def test_insert_person_in_correct_post_request(self):
        file = self.generate_test_file1()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/')

    def test_insert_not_csv(self):
        file = self.generate_test_file2()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/import_data')

    def test_insert_empty_file(self):
        file = self.generate_test_file3()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertEqual(resp.status_code, 200)

    def test_insert_file_without_attribute(self):
        file = self.generate_test_file4()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/import_data')

    def test_insert_file_mixed_atr(self):
        file = self.generate_test_file5()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/')

    def test_insert_wrond_date(self):
        file = self.generate_test_file6()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/import_data')

    def test_insert_wrong_name(self):
        file = self.generate_test_file7()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/import_data')

    def test_insert_wrong_surname(self):
        file = self.generate_test_file8()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/import_data')

    def test_insert_wrong_position(self):
        file = self.generate_test_file9()

        with open(file.name, 'rb') as f:
            resp = self.client.post('/import_data', {'file': f})
        self.assertRedirects(resp, '/import_data')


class AppFindPersonTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create(name='Ivan', surname='Seliv', birth_date='1860-05-01',
                                         position='Starter')
        test_user1.save()

    def test_search_person_in_correct_post_request1(self):
        resp = self.client.post(reverse('find_person'), {'users': 'Ivan Seliv'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'find_person.html')

    def test_search_person_in_correct_post_request2(self):
        resp = self.client.post(reverse('find_person'), {'users': 'Ivan'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'find_person.html')

    def test_search_person_in_correct_post_request3(self):
        resp = self.client.post(reverse('find_person'), {'users': ''})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'find_person.html')

    def test_search_person_in_correct_post_request4(self):
        resp = self.client.post(reverse('find_person'), {'users': 'Aadw Fefe Ufeeg'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'find_person.html')

    # main
    def test_main_correct_get_request(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main_page.html')
