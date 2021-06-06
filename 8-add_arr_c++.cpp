#include <iostream>
#include <list>
#include <string>
#include <windows.h>
#include <iostream>
#include <ctime>
#include <fstream>

using namespace std;
int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    srand(time(NULL));
    int num, size, avt, form, vm, n, dimstat;
    n = 1;
tryAgainNum:
    cout << "Виберіть розмірність масиву: 1-10, 2-100, 3-1000, 4-10000, 5-1000000000, 7-Своє число ";
    cin >> size;                                     //
    if (size == 1) num = 10;                        //
    else if (size == 2) num = 100;                 //
    else if (size == 3) num = 1000;               //
    else if (size == 4) num = 10000;             //
    else if (size == 5) num = 1000000000;       // Час створення і заповнення 55 секунд. Займа 7 Gb оперетивної памяті, може працювати лише на 64 бітних ОС
 // else if (size == 6) num = 10000000000;   // 9хв-Приблизний час автоматичного заповнення. Недостатньо ОП
    else if (size == 7) {
        cout << endl << "Введiть довжину масиву ";
        cin >> num;
    }
    else { cout << "Неправильне значення "; goto tryAgainNum; }

tryAgainAvt:
    cout << "Заповнити 1-вручну, 2-автоматично ";
    cin >> avt;
    cout << "Заповнити 1-цілими числами, 2-дробовими, 3-Символи ";
    cin >> form;
    if (size == 7) {
        dimstat=1;
    }
    else {
        cout << "1-Динамічний масив, 2-статичний ";
        cin >> dimstat;
    }
    if (dimstat == 2 && size == 5) {
        cout << "Недоступний при роботі з масивами в яких бульше 100000 елементів ";
        goto tryAgainAvt;
    }
    if (form != 1 && form != 2 && form != 3) { cout << "Неправильне значення "; goto tryAgainAvt; }
   
    unsigned int start_time = clock();                                    // Запуск таймер
                                                                         //
        int* p_darr_int = new int[num];                                 //Динамічний int
        if (form != 1 && (dimstat != 1)) delete[] p_darr_int;

        double* p_darr_double = new double[num];
        if (form != 2 && (dimstat != 1)) delete[] p_darr_double;

        char* p_darr_char = new char[num];
        if (form != 3 && (dimstat != 1)) delete[] p_darr_char;
   
    if (dimstat == 2) {                                                   //ціле/стат
        if (form == 1) {
            if (size == 1) {
               int p_darr_int[10];
            }
            if (size == 2) {
               int p_darr_int[100];
            }
            if (size == 3) {
               int p_darr_int[1000];
            }
            if (size == 4) {
               int p_darr_int[10000];
            }
            //if (size == 5) {
            //   int p_darr_int[1000000000];//общий размер массива не должен превышать 0x7fffffff байт
            //}
            //if (size == 6) {
            //   int p_darr_int[10000000000];//общий размер массива не должен превышать 0x7fffffff байт
            //}
    }
        if (form == 2) {                                            //дріб/стат
            if (size == 1) {
               double p_darr_double[10];
            }
            if (size == 2) {
                double p_darr_double[100];
            }
            if (size == 3) {
                double p_darr_double[1000];
            }
            if (size == 4) {
                double p_darr_double[10000];
            }
            //if (size == 5) {
            //    double p_darr_double[1000000000];//общий размер массива не должен превышать 0x7fffffff байт
            //}
            //if (size == 6) {
            //    double p_darr_double[10000000000];  //общий размер массива не должен превышать 0x7fffffff байт
            //}
    }
        if (form == 3) {                                            //символ/стат
            if (size == 1) {
               char p_darr_char[10];
            }
            if (size == 2) {
                char p_darr_char[100];
            }
            if (size == 3) {
                char p_darr_char[1000];
            }
            if (size == 4) {
                char p_darr_char[10000];
            }
            //if (size == 5) {
            //    char p_darr_char[1000000000];//общий размер массива не должен превышать 0x7fffffff байт
            //}
            //if (size == 6) {
            //    char p_darr_char[10000000000];//общий размер массива не должен превышать 0x7fffffff байт
            //}
        }
    }
    if (num >= 100 && avt == 1) {
        cout << "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_" << endl;
        cout << "_-_-_-_-_-_-_-_-_-_-_-_-_ УДАЧI _-_-_-_-_-_-_-_-_-_-_-_-_" << endl;
        cout << "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_" << endl;
    }
    if (avt == 1 && form==1) {
        for (int i = 0; i < num; i++) {
            cout << "Введіть елемент масиву номер " << n << " елемент масиву ";
            cin >> p_darr_int[i];
            n++;
        }
    }
    else if (avt == 1 && form==2) {
        for (int i = 0; i < num; i++) {
            cout << "Введіть елемент масиву номер " << n << " елемент масиву ";
            cin >> p_darr_double[i];
            n++;
        }
    }
    else if (avt == 1 && form==3) {
        for (int i = 0; i < num; i++) {
            cout << "Введіть елемент масиву номер " << n << " елемент масиву ";
            cin >> p_darr_char[i];
            n++;
        }
    }
    else if (avt == 2 && form == 1) {
        for (int i = 0; i < num; i++) {
            p_darr_int[i] = rand() % 100;
        }
    }
    else if (avt == 2 && form == 2) {
        for (int i = 0; i < num; i++) {
            double r = static_cast <double> (rand() % 100) / static_cast <double> (5);
            p_darr_double[i] = r;
        }
    }
    else if (avt == 2 && form == 3) {
        for (int i = 0; i < num; i++) {
            p_darr_char[i] = rand() % 255;
            if (i == 10) cout << endl;
        }
    }
    else { cout << "Неправильне значення "; goto tryAgainAvt; }
    unsigned int end_time = clock();                                        //Стоп таймер
    unsigned int search_time = (end_time - start_time);
    int n_m ;
    int size_m;
    string type_m;
    while (true)
    {
        cout<<endl << "Бажаєте: 1-вивести масив, 2-показати статистику, 3-створити файл статистики, 4-Вiдкрити файл статистики9-вихiд ";
        cin >> vm;

        if (vm == 1 && form == 1)
            for (int i = 0; i < num; i++) {
                cout << " " << p_darr_int[i];
                if (i == 10) cout << endl;
            }
        if (vm == 1 && form == 2)
            for (int i = 0; i < num; i++) {
                cout << " " << p_darr_double[i];
                if (i == 10) cout << endl;
            }
        if (vm == 1 && form == 3)
            for (int i = 0; i < num; i++) {
                cout << " " << p_darr_char[i];
                if (i == 10) cout << endl;
            }
        if (vm == 2 || vm == 3) {
            if (form == 1) {
                size_m = sizeof(int) * num;
                type_m = "int";
            }
            if (form == 2) {
                size_m = sizeof(double) * num;
                type_m = "double";
            }
            if (form == 3) {
                size_m = sizeof(char) * num;
                type_m = "char";
            }
            if (vm != 3) {
                cout << endl << "Розмiр " << size_m << " байт" << "  |Тип " << type_m << "  |Час формування " << search_time << " Мсек";
            }
        }
        if (vm == 3) {
            n_m = 0;
            ifstream file;
            string str;
            file.open("statistics.txt");
            if (file.is_open()) {
                while (!file.eof())
                {
                    str = "";
                    getline(file,str);
                    n_m++;
                }
            }
                file.close();
            ofstream stat;
            stat.open("statistics.txt", ofstream::app);
            if (!stat.is_open())
            {
                cout << "Помилка відкриття файлу!";
            }
            else {
                if (n_m == 0) n_m = 1;
                stat <<"Запит № " << n_m << " |Розмiр " << size_m << " байт" << "  |Тип " << type_m<< "  |Час формування " << search_time << " Мсек"<<endl;
            }
            stat.close();
        }
        if (vm == 4) {
            system("statistics.txt");
        }
        if (vm == 9) {
            break;
        }
    }
    if (form == 1 && (dimstat != 1)) delete[] p_darr_int;
    if (form == 2 && (dimstat != 1)) delete[] p_darr_double;
    if (form == 3 && (dimstat != 1)) delete[] p_darr_char;
}

