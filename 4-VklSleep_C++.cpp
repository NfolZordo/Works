#include <iostream>
#include <string>
#include <list>
#include <string>
#include <windows.h>
#include <iostream>
#include <ctime>
#include <fstream>
#pragma warning(disable : 4996)
using namespace std;

void doit(int menu)
{
    if (menu == 1) {
        #if defined(__linux__) // any linux distribution
        #define PLATFORM "linux"
                system("shutdown now -h");

        #elif defined(_WIN64) // any windows system
        #define PLATFORM "windows"
                system("shutdown /p");
        #else
        #define PLATFORM "Is not linux or windows"
        #endif

    }
    if (menu == 2) {
        //system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0");
        cout << "test son";
    }
    if (menu == 1) {
        #if defined(__linux__) // any linux distribution
        #define PLATFORM "linux"
                system('reboot');

        #elif defined(_WIN64) // any windows system
        #define PLATFORM "windows"
                system("shutdown /r");
        #else
        #define PLATFORM "Is not linux or windows"
        #endif
    }
}

void main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    srand(time(NULL));
    int menu, in_sek, thrTimer, in_thr,in_hour, in_min, thr_hour, thr_min, thr_sec;
    while (true)
    {
        cout << "������� ��: 1-��������� 2-����� ���, 3-������������, 666-�����  ";
        cin >> menu; 
        if (menu == 666) {
            break;
        }
        cout << "1-� ������� ��� 2-����� ������� ��� ";
        cin >> in_thr;
        if (in_thr==1){
            cout << "������ ������� ����� ";
            cin >> in_hour;
            cout << "������ ������� ������ ";
            cin >> in_min;
            cout << "������ ������� ������ ";
            cin >> in_sek;
            while (true)
            {
                time_t now = time(0);
                tm* ltm = localtime(&now);
                if (in_hour <= ltm->tm_hour && in_min <= ltm->tm_min && in_sek <=ltm->tm_sec) {
                    doit(menu);
                    break;
                }
                else { Sleep(1000); }
            }
        }
        if (in_thr==2){
            cout << "������ ����� ������ ����� ";
            cin >> thr_hour;
            cout << "������ ����� ������ ������ ";
            cin >> thr_min;
            cout << "������ ����� ������ ������ ";
            cin >> thr_sec;
            thrTimer = time(0) + thr_sec + thr_min * 60 + thr_hour * 60 * 60;
            while (true)
            {
                if (thrTimer <= time(0)) {
                    doit(menu);
                    break;
                }
                else { Sleep(1000); }
            }
        }
    }
}